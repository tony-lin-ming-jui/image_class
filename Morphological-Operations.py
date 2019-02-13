import cv2
import numpy as np
from skimage import data
import skimage.morphology as sm
import matplotlib.pyplot as plt

img=cv2.imread('007.jpg')

kernel = np.ones((3,3),np.uint8)
opening1 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations = 1)
opening2= cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations = 2)
opening3 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel,iterations =4)
#closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel,iterations = 1)

erosion1 = cv2.erode(img,kernel,iterations = 1)
erosion2 = cv2.erode(img,kernel,iterations = 2)
erosion3 = cv2.erode(img,kernel,iterations = 4)
#plt.figure(figsize =(100,100))
plt.subplot(241),plt.imshow(img),plt.title('原圖'),plt.axis('off')
plt.subplot(242),plt.imshow(opening1),plt.title('開運算'),plt.axis('off')
plt.subplot(243),plt.imshow(opening2),plt.title('開運算'),plt.axis('off')
plt.subplot(244),plt.imshow(opening3),plt.title('開運算'),plt.axis('off')


plt.subplot(245),plt.imshow(img),plt.title('原圖'),plt.axis('off')
plt.subplot(246),plt.imshow(erosion1),plt.title('腐蝕（Erosion）'),plt.axis('off')
plt.subplot(247),plt.imshow(erosion2),plt.title('腐蝕（Erosion）'),plt.axis('off')
plt.subplot(248),plt.imshow(erosion3),plt.title('腐蝕（Erosion）'),plt.axis('off')
plt.show()
