import cv2
import speech_recognition as sr
import os
from time import sleep
import numpy as np
import argparse
from wide_resnet import WideResNet
from keras.utils.data_utils import get_file

import os, random

def detect(gray,frame):
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),((x+w),(y+h)),(0,0,255),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
    return frame

r = sr.Recognizer()


with sr.Microphone() as mp:
    r.adjust_for_ambient_noise(mp,duration=2)
    print('say')
    audio = r.listen(mp)

try:
    if(r.recognize_google(audio)=="hello python"):
        print("opening camera")
        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



        video_capture = cv2.VideoCapture(0)
        while True:
            _, frame = video_capture.read()
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

            canvas = detect(gray,frame)
            cv2.imshow('Video',canvas)
            if cv2.waitKey(2) & 0xff == ord('q'):
                break

    video_capture.release()
    cv2.destroyAllWindows()

except:
    pass
