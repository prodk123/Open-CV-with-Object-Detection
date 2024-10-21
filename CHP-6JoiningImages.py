# Joining Images Together
import cv2
import numpy as np

img = cv2.imread("3.jpg")

hor = np.hstack((img, img))
ver = np.vstack((img, img))

cv2.imshow("image", hor)
cv2.imshow("v image", img)
cv2.waitKey(0)
