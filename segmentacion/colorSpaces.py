import cv2
import numpy as np
bright = cv2.imread('img/nopal.png')
sinLuz = cv2.imread('img/cubo2.png')
brightHSV = cv2.cvtColor(bright, cv2.COLOR_BGR2HSV)
brightLAB = cv2.cvtColor(bright, cv2.COLOR_BGR2LAB)
brightYCB = cv2.cvtColor(bright, cv2.COLOR_BGR2YCrCb)


bgr = [124, 132, 87]
thresh = 40

minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])

maskBGR = cv2.inRange(bright,minBGR,maxBGR)
resultBGR = cv2.bitwise_and(bright, bright, mask = maskBGR)
#convert 1D array to 3D, then convert it to HSV and take the first element
# this will be same as shown in the above figure [65, 229, 158]
hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
resultHSV = cv2.bitwise_and(brightHSV, brightHSV, mask = maskHSV)
#convert 1D array to 3D, then convert it to YCrCb and take the first element
ycb = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2YCrCb)[0][0]
minYCB = np.array([ycb[0] - thresh, ycb[1] - thresh, ycb[2] - thresh])
maxYCB = np.array([ycb[0] + thresh, ycb[1] + thresh, ycb[2] + thresh])
maskYCB = cv2.inRange(brightYCB, minYCB, maxYCB)
resultYCB = cv2.bitwise_and(brightYCB, brightYCB, mask = maskYCB)
#convert 1D array to 3D, then convert it to LAB and take the first element
lab = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2LAB)[0][0]
minLAB = np.array([lab[0] - thresh, lab[1] - thresh, lab[2] - thresh])
maxLAB = np.array([lab[0] + thresh, lab[1] + thresh, lab[2] + thresh])
maskLAB = cv2.inRange(brightLAB, minLAB, maxLAB)
resultLAB = cv2.bitwise_and(brightLAB, brightLAB, mask = maskLAB)
cv2.imshow("Original", bright)
#cv2.imshow("Preprocesado LAB", brightLAB)
#cv2.imshow("BGR", resultBGR)
cv2.imshow("HSV", resultHSV)
#cv2.imshow("YCB", resultYCB)
#cv2.imshow("LAB", resultLAB)

cv2.waitKey()