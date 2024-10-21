import cv2
import numpy as np

img = cv2.imread("4.jpg")
kernel = np.ones((5, 5), np.uint8)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # converts into grayscale image
imgBlur = cv2.GaussianBlur(img, (25, 25), 0)    # blurs the image
imgCanny = cv2.Canny(img, 100, 100)             # detects edges in image
imgDialation = cv2.dilate(imgCanny, kernel, iterations=5) #to thicken edges
imgEroded = cv2.erode(imgCanny, kernel, iterations=1)    #to thin edges

cv2.imshow("Image", imgBlur)
cv2.imshow("CannyImage", imgCanny)
cv2.imshow("Image", imgDialation)
cv2.imshow("Image", imgEroded)
cv2.waitKey(0)
