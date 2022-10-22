import cv2
import numpy as np

image = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_3\\image_input\\scenery.jpg')

#图像平移
#垂直方向 向下平移120
M = np.float32([[1, 0, 0], [0, 1, 120]])
img1 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#垂直方向 向上平移120
M = np.float32([[1, 0, 0], [0, 1, -120]])
img2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#水平方向 向右平移120
M = np.float32([[1, 0, 120], [0, 1, 0]])
img3 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#水平方向 向左平移120
M = np.float32([[1, 0, -120], [0, 1, 0]])
img4 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

#显示图像
cv2.imshow("Image", image)
cv2.imshow("Down 120", img1)
cv2.imshow("Up 120", img2)
cv2.imshow("Right 120", img3)
cv2.imshow("Left 120", img4)

#等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
