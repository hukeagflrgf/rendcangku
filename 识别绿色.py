# -*- coding: utf-8 -*-
import cv2
import numpy as np

#读取图片
src=cv2.imread("2.jpg")

#将图片转换成hsv形式
imgHSV=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

#确定绿色的区域范围
mingreen=np.array([30,60,60])
maxgreen=np.array([90,255,255])

#去背景
mask2=cv2.inRange(imgHSV,mingreen,maxgreen)
dst=cv2.bitwise_and(src,src,mask=mask2)

#显示图片
cv2.namedWindow('src',cv2.WINDOW_NORMAL)
cv2.imshow('src',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
