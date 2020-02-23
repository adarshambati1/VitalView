import math
import cv2
import numpy as np
import time
import logging

capture = cv2.VideoCapture(0)
GreenAvglist = []
RedAvglist = []
tic = time.clock()

while True:
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

    for x in range (0,340,1):
      for y in range(0,480,1):
        color = frame[y,x]
        num=num+1
        RedTotal=color[0]+RedTotal
        GreenTotal =color[1]+GreenTotal
        RedAvg = (RedTotal)/num
        GreenAvg=GreenTotal/num
    GreenAvglist.append(GreenAvg)
    RedAvglist.append(RedAvg)

    toc = time.clock()
    timer = toc -tic
    if (timer) >30:
        SampleFreq = timer/len(GreenAvglist)
        RRFreq = np.fft.rfft(GreenAvglist)
        freqs = np.fft.rfftfreq(len(RRFreq), d=SampleFreq)
	print (freqs)
        bpm_floats = map(float, freqs)
        for i in bpm_floats:
            i = 0.25
            if 0.2<=i<=0.3:
               print(i)
               bpm_range = []
               bpm_range.append(i)
               global min_bpm
               max_bpm = max(bpm_range)*60
               min_bpm = min(bpm_range)*60
               print("max_bpm: "+ str(max_bpm))
               print("min_bpm: "+ str(min_bpm))
#        print(RRFreq)
       # bpm = int(math.ceil(RRFreq*60))
        #RR1Freq = Fft.fft(RedAvgList, timer, SampleFreq)
        #bpm = int(math.ceil(RR1Freq*60))
               tic = time.clock()
               logger = logging.getLogger('log')
               hdlr = logging.FileHandler('/home/pi/final/log.csv')
               formatter = logging.Formatter('%(asctime)s,%(message)s')
               hdlr.setFormatter(formatter)
               logger.addHandler(hdlr)
               logger.setLevel(logging.INFO)
               string2 = "RR:"+str(min_bpm)
               logger.info(string2)
 #     print len(GreenAvglist)
#      print len(RedAvglist)

#    if cv2.waitKey(1) == 27:
 #       break
capture.release()
cv2.destroyAllWindows()
#print(RRFreq)
