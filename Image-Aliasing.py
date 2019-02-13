import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('005.jpg',0) #讀灰度圖像
img1 = np.float32(img) #轉乘數職類型
kernel = np.ones((15,15),np.float32)/25 #(15,15)
dst = cv2.filter2D(img1,-1,kernel)
plt.subplot(2,3,1)
plt.title('原圖')
plt.axis('off')
plt.imshow(img1,'gray')
plt.subplot(2,3,2)
plt.title('2D濾波')
plt.axis('off')
plt.imshow(dst,'gray')

#均值濾波
blur = cv2.blur(img,(15,15))#數字可替換15,15
plt.subplot(2,3,3)
plt.title('均值濾波')
plt.axis('off')
plt.imshow(blur,'gray')

blurs = cv2.GaussianBlur(img,(15,15),0)#數字可替換15,15
plt.subplot(2,3,4)
plt.title('高斯模糊')
plt.axis('off')
plt.imshow(blurs,'gray')

blurss = cv2.medianBlur(img,15)#數字可替換15
plt.subplot(2,3,5)
plt.title('中值濾波')
plt.axis('off')
plt.imshow(blurss,'gray')

blursss = cv2.bilateralFilter(img,15,90,90)#數值愈大越模糊
plt.subplot(2,3,6)
plt.title('雙邊濾波')
plt.axis('off')
plt.imshow(blursss,'gray')
plt.show()

