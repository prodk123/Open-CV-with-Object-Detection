# Color Detection

import cv2


def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue max", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Saturation min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Sturation max", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Val max", "TrackBars", 0, 255, empty)

while True:
    img = cv2.imread("9.jpg")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hmin = cv2.getTrackbarPos("Hue min", "TrackBars")
    hmax = cv2.getTrackbarPos("Hue max", "TrackBars")
    smin = cv2.getTrackbarPos("Saturation min", "TrackBars")
    smax = cv2.getTrackbarPos("Sturation max", "TrackBars")
    vmin = cv2.getTrackbarPos("Val min", "TrackBars")
    vmax = cv2.getTrackbarPos("Val max", "TrackBars")

    mask = cv2.inRange()

    cv2.imshow("img", img)
    cv2.imshow("imgHSV", imgHSV)  # hue saturation image
    cv2.waitKey(0)
