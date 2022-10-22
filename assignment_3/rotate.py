import cv2
import numpy as np

image = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_3\\image_input\\scenery.jpg')
rows, cols, channel = image.shape

# 绕图像中心旋转30度
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 30, 1)
rotateImg = cv2.warpAffine(image, M, (cols, rows))

# 显示图像
cv2.imshow("Image", image)
cv2.imshow("rotateImg", rotateImg)

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
