import numpy as np
import cv2

cam = cv2.VideoCapture(0)

subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cam.read()

    if ret:
        masked = subtractor.apply(frame)

        cv2.imshow('frame',masked)
    k = cv2.waitKey(30) & 0xff
    if k == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
