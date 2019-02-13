
import cv2
import numpy as np
#https://blog.csdn.net/lwplwf/article/details/77494072

def rgbtohsi(rgb_lwpImg):
    rows = int(rgb_lwpImg.shape[0])
    cols = int(rgb_lwpImg.shape[1])
    b, g, r = cv2.split(rgb_lwpImg)
    # 归一化到[0,1]
    b = b / 255.0
    g = g / 255.0
    r = r / 255.0
    hsi_lwpImg = rgb_lwpImg.copy()
    H, S, I = cv2.split(hsi_lwpImg)
    for i in range(rows):
        for j in range(cols):
            num = 0.5 * ((r[i, j]-g[i, j])+(r[i, j]-b[i, j]))
            den = np.sqrt((r[i, j]-g[i, j])**2+(r[i, j]-b[i, j])*(g[i, j]-b[i, j]))
            theta = float(np.arccos(num/den))

            if den == 0:
                    H = 0
            elif b[i, j] <= g[i, j]:
                H = theta
            else:
                H = 2*3.14169265 - theta

            min_RGB = min(min(b[i, j], g[i, j]), r[i, j])
            sum = b[i, j]+g[i, j]+r[i, j]
            if sum == 0:
                S = 0
            else:
                S = 1 - 3*min_RGB/sum

            H = H/(2*3.14159265)
            I = sum/3.0
            # 输出HSI图像，扩充到255以方便显示，一般H分量在[0,2pi]之间，S和I在[0,1]之间
            hsi_lwpImg[i, j, 0] = H*255
            hsi_lwpImg[i, j, 1] = S*255
            hsi_lwpImg[i, j, 2] = I*255
    return hsi_lwpImg
if __name__ == '__main__':
    rgb_lwpImg = cv2.imread("001.jpg")
    hsi_lwpImg = rgbtohsi(rgb_lwpImg)

    cv2.imshow('rgb_lwpImg', rgb_lwpImg)
    cv2.imshow('hsi_lwpImg', hsi_lwpImg)

    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        cv2.destroyAllWindows()

'''
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
#import matplotlib.image as mpimg # mpimg 用於讀取圖片
from pylab import *

img = Image.open('002.jpg')
print("原本的模式",img.mode)
print(img.getpixel((0,0)))
imcmyk=img.convert("CMYK")
print("新的模式",imcmyk.mode)
print(imcmyk.getpixel((0,0)))

plt.subplot(1,2,1)
plt.title('origin')
plt.axis('off')
plt.imshow(img)
plt.subplot(1,2,2)
plt.title('new')
plt.axis('off')
plt.imshow(imcmyk)

plt.show()
'''

