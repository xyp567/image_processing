import numpy as np
import cv2
import matplotlib.pyplot as plt

def piecewise_linear_transform(img):
    height, width = img.shape[:2]
    r1, s1 = 80, 10
    r2, s2 = 140, 200
    k1 = s1 / r1  # 第一段斜率
    k2 = (s2 - s1) / (r2 - r1)  # 第二段斜率
    k3 = (255 - s2) / (255 - r2)  # 第三段斜率

    #绘制分段线性函数
    x = np.arange(0, 256)
    y=[]
    for i in range(256):
        if x[i] < r1:
            y.append(k1 * x[i])
        elif r1 <= x[i] <= r2:
            y.append(k2 * (x[i] - r1) + s1)
        else:
            y.append(k3 * (x[i] - r2) + s2)
    plt.plot(x, y, 'r', linewidth=1)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title('分段函数')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    img_copy = np.zeros_like(img)
    for i in range(height):
        for j in range(width):
            if img[i, j] < r1:
                img_copy[i, j] = k1 * img[i, j]
            elif r1 <= img[i, j] <= r2:
                img_copy[i, j] = k2 * (img[i, j] - r1) + s1
            else:
                img_copy[i, j] = k3 * (img[i, j] - r2) + s2
    return img_copy

img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_2\\image_input\\einstein.jpg', 0)
ret = piecewise_linear_transform(img)
cv2.imshow('Image',img)
cv2.imshow('piecewise_linear',ret)
cv2.waitKey()
cv2.destroyAllWindows()
