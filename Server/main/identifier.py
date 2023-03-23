from weakref import ref
import cv2
import numpy as np
import face_recognition
from deepface import DeepFace
import os
from datetime import datetime

# from PIL import ImageGrab

class Identifier:
    def __init__(self):
        self.refresh()
        #  remove
    def refresh(self):
        self.path = os.path.join(os.getcwd(),'media/images/known_people')
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        print(self.myList)
        for cl in self.myList:
            curImg = cv2.imread(os.path.join(self.path, cl))
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        try:
            self.encodeListKnown = self.findEncodings(self.images)
        except:
            return -1
        print('Encoding Complete')
        print(self.classNames)
        return 1
        
    def findEncodings(self,images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)    
        return encodeList


    def check(self,img):
        
    # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        names = []
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
            try:
                matchIndex = np.argmin(faceDis)
            except:
                continue
            if matches[matchIndex]:
                name = self.classNames[matchIndex]
                names.append(name)
        print(names)
        return(names)