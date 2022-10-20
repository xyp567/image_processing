import numpy as np
import matplotlib.pyplot as plt
import cv2

#绘制曲线 y = c * log(1 + x)
def log_plot(c):
    x = np.arange(0, 256, 0.01)
    y = c * np.log(1 + x)
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.title('对数变换')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.xlim(0, 255), plt.ylim(0, 255)
    plt.show()

#对数变换
def log(c, img):
    output = c * np.log(1.0 + img)
    output = np.uint8(output + 0.5)
    return output

img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_2\\image_input\\einstein.jpg')
log_plot(30)
output = log(30, img)
cv2.imshow('Image', img)
cv2.imshow('nolinear', output)
cv2.waitKey(0)
cv2.destroyAllWindows()
