import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_1\\image_input\\lena.jpg', 0)
fig = plt.figure(figsize=(13, 26))
for i in range(8):
    ax = fig.add_subplot(4, 2, i+1)
    if i < 7:
        dst = np.uint(img * (2**(8- i)-1))
    else:
        dst = np.uint(img * (2))
    ax.imshow(dst, 'gray')
    ax.set_xticks([])
    ax.set_yticks([])
plt.tight_layout()
out_path = 'D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_1\\image_output\\greyscale_resolution_output.jpg'
plt.savefig(out_path)
plt.clf()
