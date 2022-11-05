import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
def diedai(img):
    img_array = np.array(img).astype(np.float32)
    I=img_array
    zmax=np.max(I)
    zmin=np.min(I)
    tk=(zmax+zmin)/2
    b=1
    m,n=I.shape;
    while b==0:
        ifg=0
        ibg=0
        fnum=0
        bnum=0
        for i in range(1,m):
             for j in range(1,n):
                tmp=I(i,j)
                if tmp>=tk:
                    ifg=ifg+1
                    fnum=fnum+int(tmp)
                else:
                    ibg=ibg+1
                    bnum=bnum+int(tmp)
        zo=int(fnum/ifg)
        zb=int(bnum/ibg)
        if tk==int((zo+zb)/2):
            b=0
        else:
            tk=int((zo+zb)/2)
    return tk
img = cv2.imread("D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_8\\image_input\\photographer.jpg")
plt.figure()
plt.hist(img.ravel(),256)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
img = cv2.resize(gray,(200,200))
yvzhi=diedai(img)
ret1, th1 = cv2.threshold(img, yvzhi, 255, cv2.THRESH_BINARY)
print(ret1)
plt.figure()
plt.hist(th1.ravel(),256)
plt.figure()
plt.imshow(th1,cmap=cm.gray)
plt.show()
