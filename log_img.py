import numpy as np
import cv2

img_1=cv2.imread('001.jpg')

img_2=np.uint8(np.log(img_1))

thresh=1 #THRESH_BINARY 2值化
#img_3=cv2.threshold(img_2,thresh, 255,cv2.THRESH_BINARY)[1]
img_3=cv2.threshold(img_2,thresh, 255,cv2.NORM_MINMAX)

cv2.imshow('input',img_1)

cv2.imshow('log',img_3)
cv2.waitKey(0)
cv2.destroyAllwindows()
