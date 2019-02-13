import cv2
import numpy as np
from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt

img=cv2.imread('009.jpg')

kernel = np.ones((3,3),np.uint8)

closing1 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations = 11)
closing2 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations = 12)
closing3 = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations = 14)



plt.subplot(241),plt.imshow(img),plt.title('原圖'),plt.axis('off')
plt.subplot(242),plt.imshow(closing1),plt.title('閉運算'),plt.axis('off')
plt.subplot(243),plt.imshow(closing2),plt.title('閉運算'),plt.axis('off')
plt.subplot(244),plt.imshow(closing3),plt.title('閉運算'),plt.axis('off')


dilation1 = cv2.dilate(img,kernel,iterations = 5)
dilation2 = cv2.dilate(img,kernel,iterations = 9)
dilation3 = cv2.dilate(img,kernel,iterations = 12)
plt.subplot(245),plt.imshow(img),plt.title('原圖'),plt.axis('off')
plt.subplot(246),plt.imshow(dilation1),plt.title('膨脹（Dilation）'),plt.axis('off')
plt.subplot(247),plt.imshow(dilation2),plt.title('膨脹（Dilation）'),plt.axis('off')
plt.subplot(248),plt.imshow(dilation3),plt.title('膨脹（Dilation）'),plt.axis('off')
plt.show()
