import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
	print("Error opening")

while cap.isOpened():
	ret, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

	if ret:
		cv2.imshow('Frame', gray)
		
		if cv2.waitKey(25) & 0xff == ord('q'): break


cap.release()

cv2.destroyAllWindows()
