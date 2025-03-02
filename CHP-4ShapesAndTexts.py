#Shapes and Texts on Images
import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)
img[200:300, 300:600] = (255,0,0) # colors image with blue color for particular part

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,255), 3) # (img, starting position, ending position, color, thickness)

cv2.rectangle(img, (0,0), (400,450), (255,0,255), cv2.FILLED)
cv2.circle(img, (400,50), 40, (0,255,0),  cv2.FILLED)

#Text on images
cv2.putText(img, "Hello World", (200,300), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 2) #(img, text, starting position, font, scale(size), color, thickness)
cv2.imshow("img", img)
cv2.waitKey(0)