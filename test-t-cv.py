#需安裝Anaconda環境
#安裝套件: 1.pip install opencv-python


import numpy as np
import cv2

print("請將圖片放到該資料夾中")
#try:
    ##pic=input("輸入圖片檔名(例如:001.jpg):")
    #pic='001.jpg'
img = cv2.imread('001.jpg')
    ##img = cv2.imread(pic)
#灰階
'''
img_gray = cv2.imread('001.jpg', cv2.IMREAD_GRAYSCALE)#灰階
print(type(img))
cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)
cv2.imshow('My Image',img_gray)
    #cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
image_log = np.uint8(np.log(np.array(img) +1)) #最後UINT8 先乘255除最大直 
cv2.normalize(image_log, image_log,0,255,cv2.NORM_MINMAX)
#    轉換成8bit圖像顯示
#cv2.convertScaleAbs(image_log,image_log)
cv2.imshow('image_log',image_log)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''

    #res = np.uint8(np.clip((1.5 * img + 10), 0, 255))
    #0~255 調整圖片亮度
    print("數字越大越亮越小越暗")
    ##y = input("輸入0~255的數字調整圖片光暗:")
    #print(type(y))
    res= np.uint8(np.clip((1.5*img + 10), 0,230))
    ##res= np.uint8(np.clip((1.5*img + 10), 0,int(y)))
    tmp = np.hstack((img, res))  # 两张图片横向合并（便于对比显示）
    cv2.imshow('original',img)
    cv2.imshow('new',res)
    #cv2.imshow(u'all', tmp)
    cv2.waitKey(0)
'''
#except Exception:
    #print("沒有"+pic+"這張圖片,或沒家副檔名")
