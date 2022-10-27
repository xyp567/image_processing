import cv2
import numpy as np
import random as rd
import math
from scipy.signal import wiener

def gauss_noise(image, mean=0, var=0.001):
    image = np.array(image/255, dtype=float)
    noise = np.random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out*255)
    return out

def sport_noise_2(im,ang,dist):
    Sport_mask = np.zeros(im.shape[:2])
    xc = im.shape[0]//2
    yc = im.shape[1]//2
    if ang > 180:
        ang = ang % 180
    sin_val = math.sin(ang * math.pi / 180)
    cos_val = math.cos(ang * math.pi / 180)
    for i in range(dist):
        xo = round(sin_val * i)
        yo = round(cos_val * i)
        Sport_mask[int(xc + xo),int(yc + yo)] = 1
    return Sport_mask / Sport_mask.sum()

def pro_sport_image(im,mask):
    im = im/255
    im_fft = np.fft.fft2(im)
    mask_fft = np.fft.fft2(mask)
    im_noise = np.fft.ifft2(im_fft * mask_fft)
    im_noise = np.abs(np.fft.fftshift(im_noise))
    return im_noise

def sport_noise(im,ang,dist,k=1):
    mask = sport_noise_2(im,ang,dist)
    if len(im.shape) == 2:
        image = pro_sport_image(im,mask)
        return image * k
    elif len(im.shape) == 3:
        bgr = cv2.split(im)
        new_bgr = []
        for i in range(len(bgr)):
            image = pro_sport_image(bgr[i],mask)
            new_bgr.append(image)
        image = cv2.merge(tuple(new_bgr))
        return image * k

def wiener_filter_2(im,S,eps,SNR):
    im_fft = np.fft.fft2(im)
    S_fft = np.fft.fft2(S) + eps
    WN_fft = np.conj(S_fft)/(np.abs(S_fft)**2 + SNR)
    inv_fft = np.fft.ifft2(im_fft * WN_fft)
    inv_fft = np.abs(np.fft.fftshift(inv_fft))
    return inv_fft

def wiener_filter(im,S,eps,SNR):
    if len(im.shape) == 2:
        wn_image = wiener_filter_2(im,S,eps,SNR)
        return (wn_image*255).astype('uint8')
    elif len(im.shape) == 3:
        bgr = cv2.split(im)
        new_bgr = []
        for i in range(len(bgr)):
            img = wiener_filter_2(bgr[i],S,eps,SNR)
            new_bgr.append(img)
        wn_image = cv2.merge(tuple(new_bgr))
        return (wn_image*255).astype('uint8')

view = cv2.imread('D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_6\\image_input\\lena.jpg')
if view.shape[-1] == 3:
    view = cv2.cvtColor(view, cv2.COLOR_BGR2GRAY)
else:
    view = view.copy()
gauss_view = gauss_noise(view)
sport_view = sport_noise(view.copy(),ang=20,dist=20,k=1)
gauss_sport_view = sport_noise(gauss_view.copy(),ang=20,dist=20,k=1)
S = sport_noise_2(sport_view,ang=20,dist=20)
wn_gauss_sport_view1 = wiener_filter(gauss_sport_view.copy(),S,0.01,SNR=0.00)
wn_gauss_sport_view2 = wiener_filter(gauss_sport_view.copy(),S,0.01,SNR=0.01)
lenaNoise = gauss_view.astype('float64')
lenaWiener = wiener(lenaNoise, [3, 3])
lenaWiener = np.uint8(lenaWiener / lenaWiener.max() * 255)

cv2.imshow('Image',view)
cv2.imshow('noise_image',gauss_sport_view)
cv2.imshow('SNR_unknown',wn_gauss_sport_view1)
cv2.imshow('SNR_known',wn_gauss_sport_view2)
cv2.imshow('Function_known',lenaWiener)

cv2.waitKey(0)
cv2.destroyAllWindows()
