#pip install skimage
from skimage import data, exposure, img_as_float
import matplotlib.pyplot as plt
import matplotlib.image as mpimg # mpimg 用於讀取圖片
from pylab import *
import numpy as np
print("請將圖片放到該資料夾中")
pic=input("輸入圖片檔名(例如:001.jpg):")
imag = mpimg.imread(pic)
#imag = mpimg.imread('001.jpg')
#image=img_as_float(imag)#變浮點數
# 使用伽馬調整# 第二個引數控制亮度，大於1增強亮度，小於1降低
gam1= exposure.adjust_gamma(imag, 2)   #調暗
gam2= exposure.adjust_gamma(imag, 0.5)#調亮
#gam3= exposure.adjust_log(imag ,1)#-1是相機底片浮點不能用
#a=gam3                             
plt.figure('picture',figsize=(19,19))
plt.subplot(2,3,1)
plt.title('origin')
plt.axis('off')
plt.imshow(imag,plt.cm.gray)
plt.subplot(2,3,4)
plt.hist(imag.ravel(),256,[0,256]);

plt.subplot(2,3,2)
#plt.subplot(142)
plt.title('dark')
plt.axis('off')
plt.imshow(gam1,plt.cm.gray)
plt.subplot(2,3,5)
plt.hist(gam1.ravel(),256,[0,256]);

plt.subplot(2,3,3)    
#plt.subplot(143)
plt.title('bright')
plt.axis('off')
plt.imshow(gam2,plt.cm.gray)
plt.subplot(2,3,6)
plt.hist(gam2.ravel(),256,[0,256]);
plt.show()
#plt.axis('off')
'''
    plt.subplot(144)
    plt.title('log')
    plt.imshow(gam3,plt.cm.gray)
    plt.axis('off')

'''    


#except Exception:
    #print("沒有"+pic+"這張圖片,或沒加副檔名")
    #pass
#
