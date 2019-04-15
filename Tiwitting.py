import sys
#import picamera
import numpy as np
import cv2
from twython import Twython
CONSUMER_KEY = 'DNmNg4stOEBMMIcLzsJlnXI3Z'
CONSUMER_SECRET = 'rYnj1WF7Nr5u6w0CE1iGMZkX0rHFIFsGtq6tX30nGdyfRSgHHI'
ACCESS_KEY = '999715839342505984-98m48o9S1OonRi7BkaY6nZGjra5J83z'
ACCESS_SECRET = 'BdINg11nhqwrSbyXxlytsG7Ihzgkx5U3zPiCxiHzWtLSq'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET) 
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
gray =cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
photo =cv2.imwrite( "Gray_Image.jpg", gray  );
pp=open("Gray_Image.jpg",'rb')
response = api.upload_media(media=pp)


#camera=picamera.PiCamera()
#camera.resolution = (1024, 768)
#camera.capture('image.jpg')
#photo=open('image.jpg','rb')
api.update_status(status=sys.argv[1],media_ids=[response['media_id']])
#api.update_status(status=sys.argv[1])
cap.release()
cv2.destroyAllWindows()