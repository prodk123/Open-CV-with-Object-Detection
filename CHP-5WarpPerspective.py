# Warp Perspective
#   - Warp Perspective: This is a more advanced technique that uses a 3D model of
#     the scene to create a more realistic perspective effect. It can be used to
#     create a sense of depth and distance in an image.
import cv2
import numpy as np

img = cv2.imread("6.jpg")
width, height = 250,350

pts1 = np.float32([[111,219], [287,188], [154,482], [352,440]])
pts2= np.float32([[0,0], [width, 0], [0,height], [width, height]])
mat = cv2.getPerspectiveTransform(pts1,pts2) # array of pixels
output = cv2.warpPerspective(img, mat, (width, height)) #img,matrix,(width,height)

cv2.imshow("img", img)
cv2.imshow("img", output)
cv2.waitKey(0)