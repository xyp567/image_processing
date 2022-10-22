#先水平镜像，再绕图像中心旋转30度，最后沿垂直方向向上平移120
import cv2
import numpy as np

img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_3\\image_input\\scenery.jpg',1)
cv2.imshow('Image', img)

imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
deep= imgInfo[2]

#水平镜像
horizontalImgInfo = (height, width, deep)
horizontal = np.zeros(horizontalImgInfo,np.uint8)
for i in range(0,height):
    for j in range(0,width):
        horizontal[i, width-j-1] = img[i, j]

#绕图像中心旋转30度
M = cv2.getRotationMatrix2D((width / 2, height / 2), 30, 1)
rotateImg = cv2.warpAffine(horizontal, M, (width, height))

#垂直方向 向上平移120
M = np.float32([[1, 0, 0], [0, 1, -120]])
compositeImg = cv2.warpAffine(rotateImg, M, (rotateImg.shape[1], rotateImg.shape[0]))

cv2.imshow('compositeImg', compositeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
