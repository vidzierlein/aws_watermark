import cv2
import numpy as np


im = cv2.imread('Hurricane ridge.jpg')
img = cv2.imread("Radiant-Watermark-Transparent-copy.png")
both = np.hstack((im,img))
cv2.imshow('imgc',both)
cv2.waitKey(10000)