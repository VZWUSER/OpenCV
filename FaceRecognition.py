import cv2
import numpy as np


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')

while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
            roi_gray = gray[y:y+h,x:x+w]
            roi_color=img[y:y+h,x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_color)
            for(ex,ey,ew,eh) in eyes:
                #cv2.circle(img,(ex,ey),10,(0,255,0),2)
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            smile = smile_cascade.detectMultiScale(gray,1.5,5)
            for (x, y, w, h) in smile:
                cv2.rectangle(faces, (x, y), (x + w, y + h), (255, 128, 22), 3)
        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
           break

cap.release()
cv2.destroyAllWindows()
