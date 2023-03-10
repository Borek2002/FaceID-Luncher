import numpy as np
import cv2 as cv2

def faceID():

    faceCascade=cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    cap=cv2.VideoCapture(0)
    while(True):
        ret,frame=cap.read()
        grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(grey,scaleFactor=1.5,minNeighbors=5)
        cv2.imshow('frame',frame)
        if cv2.waitKey(20)&0xff==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()