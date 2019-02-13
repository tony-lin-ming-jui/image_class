import cv2
image = cv2.imread('005.jpg',0)

cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]
 
# 对使用不同大小的内核对原图像进行平均模糊
for (kX, kY) in kernelSizes:
    blurred = cv2.blur(image, (kX, kY))

    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

