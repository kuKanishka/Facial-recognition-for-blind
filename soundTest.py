#!/usr/bin/env python
from gtts import gTTS
import os

def voice(faces):
    for i in faces:
        print(i)
        message = gTTS(i)
        message.save("message.mp3")
        os.system('mpg321 message.mp3')