import cv2
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']

np.seterr(divide='ignore',invalid='ignore')
img = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_4\\image_input\\lena.jpg', 0)
f = np.fft.fft2(img, axes=(0, 1))
fshift = np.fft.fftshift(f)

#幅度谱
res = np.log(np.abs(fshift))
#相位谱
ag=np.angle(fshift)

#利用相位谱逆变换
ishift = np.fft.ifftshift(ag)
iimg = np.fft.ifft2(ishift)
iimg = np.abs(iimg)

#利用幅度谱逆变换
ishift1 = np.fft.ifftshift(res)
iimg1 = np.fft.ifft2(ishift1)
iimg1 = np.abs(iimg1)

#整体逆变换
ishift2=np.fft.ifftshift(fshift)
iimg2=np.fft.ifft2(ishift2)
iimg2=np.abs(iimg2)

plt.figure(figsize=(6, 4))
plt.subplot(231), plt.imshow(img, 'gray'), plt.title('原图')
plt.axis('off')
plt.subplot(232), plt.imshow(res, 'gray'), plt.title('幅度谱变换')
plt.axis('off')
plt.subplot(233), plt.imshow(ag, 'gray'), plt.title('相位谱变换')
plt.axis('off')
plt.subplot(234), plt.imshow(iimg2, 'gray'), plt.title('方式1')#整体逆变换
plt.axis('off')
plt.subplot(235), plt.imshow(iimg1, 'gray'), plt.title('方式2')#幅度谱逆变换
plt.axis('off')
plt.subplot(236), plt.imshow(iimg, 'gray'), plt.title('方式3')#相位谱逆变换
plt.axis('off')
out_path = 'D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_4\\results\\discrete_fourier_transform_result.jpg'
plt.savefig(out_path)
plt.clf()
