import math
import cv2
import numpy as np
import time
import statistics
from statistics import mean
import logging
capture = cv2.VideoCapture(0)

BlueAvglist = []
GreenAvglist = []
RedAvglist = []
BloodColorDeltaList = []
tic = time.clock()

maxDelta=0
minDelta=0

"""
Oximeter .. this code MUST operate on a Region of Interest (ROI) not on the 
whole frame. It must also be in a loop.  It works by checking the difference 
between the Red and Blue across multiple frames. When the heart beats there 
is a difference in oxygenated blood that should be revealed. If the blood is
not very oxygenated there won't be a big change in the amount of red in the 
ROI compared to the blue.
"""
counter2 = 0
for i in range(60):
    ret, frame = capture.read()
    """
    cap = cv2.imshow('video', frame)
    x = capture.set(cv2.CAP_PROP_FRAME_WIDTH,340)
    y = capture.set(cv2.CAP_PROP_FRAME_WIDTH,480)
    print("here")
    """
    cap = cv2.resize(frame, (340, 480))
    RedAvg=0.0
    num=0.0
    RedTotal=0.0
    GreenTotal=0.0
    BlueTotal=0.0

    for x in range (0,340,1):
      for y in range(0,480,1):
        color = frame[y,x]
        num=num+1
        RedTotal=color[0]+RedTotal
        GreenTotal =color[1]+GreenTotal
        BlueTotal =color[2]+BlueTotal

        RedAvg = (RedTotal)/num
        GreenAvg=GreenTotal/num
        BlueAvg=BlueTotal/num
        #BRdelta = BlueAvg - RedAvg
    counter2 = counter2+1
    GreenAvglist.append(GreenAvg)
    RedAvglist.append(RedAvg)
    BlueAvglist.append(BlueAvg)

    DCBlue = mean(BlueAvglist)
    DCRed =  mean(RedAvglist)
    ACBlue = statistics.pstdev(BlueAvglist)
    ACRed = statistics.pstdev(RedAvglist)
   # print(DCBlue,DCRed, ACBlue, ACRed)
    if counter2 >= 15:
       bloodo2 = 100-5*((ACRed/DCRed)/(ACBlue/DCBlue))
       print(bloodo2)
       logger = logging.getLogger('log')
       hdlr = logging.FileHandler('/home/pi/final/log.csv')
       formatter = logging.Formatter('%(asctime)s,%(message)s')
       hdlr.setFormatter(formatter)
       logger.addHandler(hdlr)
       logger.setLevel(logging.INFO)
       string2 = "SpO2:"+str(bloodo2)
       logger.info(string2)

       if counter2 >=30:
           counter2 =0


'''    BRdelta = max(BlueAvglist) - max(RedAvglist)
    print ("BRdelta: ", BRdelta)
    if BRdelta > maxDelta:
       maxDelta = BRdelta
    if BRdelta < minDelta:
       minDelta = BRdelta

    BlueVsRedDeltaInFrame=maxDelta - minDelta
    BloodColorDeltaList.append(BlueVsRedDeltaInFrame)

UnCalibratedBloodOxygenValue = max(BloodColorDeltaList) - min (BloodColorDeltaList)

print ("Uncalibrated blood oxygen value: " + str(UnCalibratedBloodOxygenValue))
'''
capture.release()

cv2.destroyAllWindows()

#print(RRFreq)
