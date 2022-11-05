import cv2
from matplotlib import pyplot as plt

image = cv2.imread("D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_8\\image_input\\photographer.jpg")
plt.figure()
plt.hist(image.ravel(),256)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret1, th1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
plt.figure()
plt.hist(th1.ravel(),256)
plt.figure()
plt.imshow(th1, "gray")
plt.show()
