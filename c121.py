import cv2
import numpy as np
import time 

#To Save the video captured we are using 4 bytes

fourC=cv2.VideoWriter_fourcc(*'XVID')
outPutFIle=cv2.VideoWriter('file1.avi',fourC,20.0,(640,480))

video=cv2.VideoCapture(0)
time=time.sleep(2)

backgroundImage=0

for i in range(60):
    dummy,video1=video.read()

backgroundImage=np.flip(video1,axis=1)

while(video.isOpened()):
    dummy,video1=video.read()
    if not dummy:
        break
    flipImage=np.flip(video1,axis=1)

    # converting Color

    color=cv2.cvtColor(flipImage, cv2.COLOR_BGR2HSV)

    #Creating marker to identfy the red colors

    lowerRed=np.array([0,120,60])
    upperRed=np.array([10,255,255])

    mask1=cv2.inRange(color, lowerRed, upperRed)

    lowerRed2=np.array([170,120,70])
    upperRed2=np.array([170,180,255])

    mask2=cv2.inRange(color, lowerRed2, upperRed2)

    mask3=mask1+mask2

    Finalmask1=cv2.morphologyEx(mask3,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))

    Finalmask1=cv2.morphologyEx(mask3,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    Finalmask2=cv2.bitwise_not(Finalmask1)

    WithOutRed=cv2.bitwise_and(flipImage, flipImage,mask=Finalmask2)

    WithRed=cv2.bitwise_and(backgroundImage, backgroundImage,mask=Finalmask1)

    FinalOutput=cv2.addWeighted(WithOutRed, 1, WithRed, 1, 0)

    outPutFIle.write(FinalOutput)

    cv2.imshow('Window One',FinalOutput)

    cv2.waitKey(0)

video.release()

cv2.destroyAllWindows()