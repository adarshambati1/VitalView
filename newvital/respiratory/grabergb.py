import cv2 
import numpy as np  

cap = cv2.imread('sample1.jpg')
RedAvg=0.0
num=0.0
RedTotal=0.0
GreenTotal=0.0
GreenAvglist = []
RedAvglist = []
#You're free to do a resize or not, just for the example
cap = cv2.resize(cap, (340,480))
for x in range (0,340,1):
    for y in range(0,480,1):
        color = cap[y,x]
        num=num+1
        RedTotal=color[0]+RedTotal
	GreenTotal =color[1]+GreenTotal
        RedAvg = (RedTotal)/num
        GreenAvg=GreenTotal/num
        GreenAvglist.append(GreenAvg)
	RedAvglist.append(RedAvg)
print len(GreenAvglist)
print len(RedAvglist)

