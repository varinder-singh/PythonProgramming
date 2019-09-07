import cv2
import numpy as np
import argparse

# Image path to the image will be produced at the run time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())


image = cv2.imread(args["image"])
output = image.copy()
# Need to check if the image is loaded properly.
# cv2.imshow("watch", output)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# detect circles in the image

circles =cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 75)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")

    for (x, y, r) in circles :
        cv2.circle(output, (x,y), r, (0, 255, 0), 4)
        cv2.rectangle(output,(x-5, y-5), (x+5, y+5), (0, 128, 255), -1)

    cv2.imshow("output", np.hstack([image, output]))
    cv2.waitKey(0)
