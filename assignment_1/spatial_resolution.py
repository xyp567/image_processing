import cv2
import numpy as np
import matplotlib.pyplot as plt

def down_sample(image):
    height, width = image.shape[:2]
    dst = np.zeros([height//2, width//2])
    dst = image[::2, ::2]
    return dst

img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_1\\image_input\\lena.jpg', 0)

img_2 = down_sample(img)
img_3 = down_sample(img_2)
img_4 = down_sample(img_3)

plt.figure(figsize=(15, 15))
plt.subplot(221), plt.imshow(img, 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(img_2, 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(img_3, 'gray'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img_4, 'gray'), plt.xticks([]), plt.yticks([])
plt.tight_layout()
out_path = 'D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_1\\image_output\\spatial_resolution_output.jpg'
plt.savefig(out_path)
plt.clf()
