import numpy as np
import cv2 as cv

# facial cascades
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# Classifications should match directory
people = ['Chris Evans','Dion Fonseca', 'Robert Downey Junior', 'Sebastian Stan']

# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

# provide your image Directory here
img = cv.imread(r'C:\Users\John Pan\Documents\Projects\Simple-Facial-Recognition\Photos\val\sebasval\sebaslonghairval3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Person', gray)

# Detect the face in the image
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in face_rect:
    faces_roi = gray[y:y+h, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)