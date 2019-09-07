import cv2
import argparse
import numpy as np

# Parse the run time arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help="path to image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])

# set the boundaries of the image

boundaries = [([17, 15, 100], [50, 56, 200]),
              ([86, 31, 4], [220, 88, 50]),
              ([25, 146, 190], [62, 174, 250]),
              ([103, 86, 65], [145, 133, 128])]

# loop and detect the color in the image

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")

    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(image, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)

    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)

