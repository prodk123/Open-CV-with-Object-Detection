#Resizing and Cropping Image

import cv2

img = cv2.imread("5.jpg")
print(img.shape) # gives shape of image as (height, width, no. of BGR)

imgResize = cv2.resize(img, (300, 200)) #(image , (new-width, new-height))

imgCropped = img[0:200, 200:500] #can be used as matrix(range of heights, range of widths)
cv2.imshow("Image", img) 
cv2.imshow("ImageResized", imgResize)
cv2.imshow("ImageCropped", imgCropped)
cv2.waitKey(0)