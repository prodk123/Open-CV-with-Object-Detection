import cv2

# IMAGE READING

img = cv2.imread("3.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)


# VIDEO CAPTURING
cap = cv2.VideoCapture("bikes.mp4")
while True:
    # (success boolean variable wheter sucqcessfully read or not)
    success, img1 = cap.read()
    cv2.imshow("Video", img1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# WEBCAM USAGE

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10, 100)
while True:
    # (success boolean variable wheter sucqcessfully read or not)
    success, img1 = cap.read()
    cv2.imshow("Video", img1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break