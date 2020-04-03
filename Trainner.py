import os
import pyttsx3
import cv2
from PIL import Image
import numpy as np


recogniter = cv2.face.LBPHFaceRecognizer_create()
path = "E:\\Image\\Faces"

def getIDnImage(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)] #Here os is used to access files in specifies folders and using listdir it is listing all files and using joint() it appending filename in f variable with path
    face = []
    Ids = []
    for imagePath in imagePaths:
        fimg = Image.open(imagePath).convert('L')   #here we are opening file and converting it to Gray scale
        Fnp = np.array(fimg, 'uint8') #now converting file to numpy array

        ID = int(os.path.split(imagePath)[-1].split('.')[0]) #here we spliting path of file to only file name using [-1] parameter then we again split file name in parts and taking second parameter using [1] to get ID

        face.append(Fnp) #appending numpay array to list
        print(ID)
        Ids.append(ID) #appending ID to list
        cv2.imshow('Training chalri hai Bhai', Fnp)
        #cv2.waitKey(100)
    return face, Ids


Face, IDS = getIDnImage(path)
recogniter.train(Face, np.array(IDS))
print("Complete!!")
#speak("Bring your face in front of system camera for authentication")


def TakeId():
    eye = cv2.CascadeClassifier('C:\\Users\\User\\PycharmProjects\\SystemX\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
    faceCascade = cv2.CascadeClassifier('C:\\Users\\User\\PycharmProjects\\SystemX\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(1)
    iDD = 0
    ID = 0
    while True:

        ret, im = cap.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 1)
        for (x, y, w, h) in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (225, 0, 0), 1)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = im[y:y+h, x:x+w]
            eyes = eye.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 125, 255), 2)
                Id, conf = recogniter.predict(gray[y:y + h, x:x + w])
                print(conf)
                if (conf < 47):
                    ID = 1
                    cv2.putText(im,"Access Granted", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                else:
                    ID = 0
                    cv2.putText(im,"Access Denied", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Finally!!!!', im)
        if cv2.waitKey(1) == 13:
            break
    cap.release()
    cv2.destroyAllWindows()
    return ID
