import numpy as np
origin = open("./origin.yuv", "rb")
rebuild8 = open("./lena_re.yuv", "rb")
ori = []
re8 = []
i = 0
while i < 256 * 256:
    i += 1
    buf = origin.read(1)
    buf8 = rebuild8.read(1)
    if buf:
        buf = int.from_bytes(buf, byteorder='big')
        buf8 = int.from_bytes(buf8, byteorder='big')
        ori.append(buf)
        re8.append(buf8)
u1=ori[0]
u2=ori[1]
c1=re8[0]
c2=re8[1]
sigx=ori
sigy=ori
sigxy=sigx*sigy
SSIM=((2*u1*u2+c1)*(2*sigxy+c2))/((u1*u1+u2*u2+c1)*(sigx*sigx+sigy*sigy+c2))
print(SSIM)
MSE8 = 0
for idx, _ in enumerate(ori):
    MSE8 += (ori[idx] - re8[idx]) ** 2
MSE8 /= (256 * 256)
PSNR8 = 10 * np.log10((255 ** 2) / MSE8)
print(PSNR8)
