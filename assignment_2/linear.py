import cv2
import numpy as np

img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_2\\image_input\\einstein.jpg')

# 图像灰度转换
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

height = grayImage.shape[0]
width = grayImage.shape[1]
cv2.imshow("Gray Image", grayImage)

# 1、图像灰度上移变换 DB=DA+60
result1 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        if (int(grayImage[i, j] + 60) > 255):
            gray = 255
        else:
            gray = int(grayImage[i, j] + 60)
        result1[i, j] = np.uint8(gray)
cv2.imshow("DB = DA + 60", result1)

#2、输出灰度扩展，整体变亮 DB=DA×1.6
result2 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        if (int(grayImage[i, j] * 1.6) > 255):
            gray = 255
        else:
            gray = int(grayImage[i, j] * 1.6)
        result2[i, j] = np.uint8(gray)
cv2.imshow("DB = DA * 1.6", result2)

#3、输出灰度压缩，整体变暗 DB=DA×0.6
result3 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        gray = int(grayImage[i,j]*0.6)
        result3[i,j] = np.uint8(gray)
cv2.imshow("DB = DA * 0.6", result3)

#4、图像灰度反色变换 DB=255-A
result4 = np.zeros((height, width), np.uint8)
for i in range(height):
    for j in range(width):
        gray = 255 - grayImage[i,j]
        result4[i,j] = np.uint8(gray)
cv2.imshow("DB = 255 - DA", result4)

cv2.waitKey(0)
cv2.destroyAllWindows()
