import cv2
import numpy as np
import uuid
import glob
import os

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')


def makemovie(filename,hastitle):
    img_array = []
    font = cv2.FONT_HERSHEY_COMPLEX
    org = (400, 50)
    fontscale = 1
    color = (0, 0, 0)
    thickness = 3
    size = (1, 1)
    titlelen = 15
    searchword = filename
    framerate = 60
    loc = 'images/'
    if hastitle:
        print('adding title')
        img = cv2.imread('images/title.jpg')
        height, width, layers = img.shape
        size = (width, height)
        print('adding title frames')
        for i in range(1, titlelen):
            img_array.append(img)
    print('reading all images')
    for filename in sorted(glob.glob(loc + '*.jpg')):
        img = cv2.imread(filename)
        img = cv2.putText(img, filename.replace('_trump.jpg', '').replace(loc, ''), org, font, fontscale, color, thickness,
                          cv2.LINE_AA)
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)

    print('setting out')
    out = cv2.VideoWriter('videos/' + searchword + '.mp4', cv2.VideoWriter_fourcc(*'MP4V'),
                          framerate, size)  # *'MP4V'
    print('adding all frames')
    for i in range(len(img_array)):
        # if i> titlelen:
        # for k in range(20,100,20):
        # out.write(cv2.blur(img_array[i],(k,k)) )
        for j in range(1, 15):
            out.write(img_array[i])
            # for k in range(100,10,-10):
            # out.write(cv2.blur(img_array[i],(k,k)) )
    out.release()
    print('Done')







files = glob.glob('images/*')
for f in files:
    os.remove(f)

for x in range(50):
        ret, img = cap.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.1,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
            filename = str('images/'+uuid.uuid4().hex) + ".jpg"
            cv2.imwrite(filename,img[y:y+h, x:x+w])
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

makemovie('momo',False)
cap.release()
cv2.destroyAllWindows()
