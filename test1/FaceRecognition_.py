import face_recognition
import cv2
import soundTest
# capture live feed
video_capture = cv2.VideoCapture(0)
#load images
akshaya_img = face_recognition.load_image_file("images/akshaya.jpeg")
sanjay_img = face_recognition.load_image_file("images/sanjay.jpeg")
kan_img = face_recognition.load_image_file("images/kanishka1.jpeg")

#encode images
akshaya_encoding = face_recognition.face_encodings(akshaya_img)[0]
sanjay_encoding = face_recognition.face_encodings(sanjay_img)[0]
kan_encoding = face_recognition.face_encodings(kan_img)[0]

#store encodings
known_face_encodings = [akshaya_encoding, sanjay_encoding, kan_encoding]

#face names
known_face_names = ['Akshaya', 'Sanjay', 'Kanishka']

#variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx = 0.25, fy = 0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if process_this_frame:
        #find all faces
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = 'Unknown'

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)
            
    process_this_frame = not process_this_frame

    for(top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        #draw rectangle over the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        #label the face
        cv2.rectangle(frame, (left, bottom-35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left +6, bottom - 6), font, 1.0, (255,255,255), 1)

    #output
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()


