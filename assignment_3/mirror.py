import cv2
import numpy as np

img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_3\\image_input\\scenery.jpg',1)
cv2.imshow('Image', img)

imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep= imgInfo[2]

#垂直镜像
verticalImgInfo = (height, width, deep)
vertical = np.zeros(verticalImgInfo,np.uint8)
for i in range(0,height):
    for j in range(0,width):
        vertical[height-i-1, j] = img[i, j]

#水平镜像
horizontalImgInfo = (height, width, deep)
horizontal = np.zeros(horizontalImgInfo,np.uint8)
for i in range(0,height):
    for j in range(0,width):
        horizontal[i, width-j-1] = img[i, j]

cv2.imshow('vertical_mirror',vertical)
cv2.imshow('horizontal_mirror', horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
