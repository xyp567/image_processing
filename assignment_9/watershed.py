import cv2 as cv
import numpy as np
def watearshel_demo():
    blured = cv.pyrMeanShiftFiltering(img, 10, 80)
    gray = cv.cvtColor(blured, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (1, 1))
    mb = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=2)
    sure_bg = cv.dilate(mb, kernel, iterations=3)
    dist = cv.distanceTransform(mb, cv.DIST_L2, 3)
    dist_output = cv.normalize(dist, 0, 1.0, cv.NORM_MINMAX)
    ret, surface = cv.threshold(dist, dist.max() * 0.6, 255, cv.THRESH_BINARY)
    surface_fg = np.uint8(surface)
    unknow = cv.subtract(sure_bg, surface_fg)
    ret, markers = cv.connectedComponents(surface_fg)
    markers = markers + 1
    markers[unknow == 255] = 0
    markers = cv.watershed(img, markers=markers)
    img[markers == -1] = [0, 0, 255]
    cv.imshow('result', img)
filepath = "D:\\Projects\\PycharmProjects\\ImageAnalysisProject\\assignment_9\\image_input\\circle.jpg"
img = cv.imread(filepath)
cv.imshow("image", img)
watearshel_demo()
cv.waitKey(0)
cv.destroyAllWindows()
