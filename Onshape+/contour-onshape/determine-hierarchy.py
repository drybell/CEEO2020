import cv2
import numpy as np
import sys
np.set_printoptions(threshold=sys.maxsize)

# REMOVE A CONTOUR WITHOUT A PARENT AND ITS FIRST CHILD 

image = cv2.imread("multiple-holes.jpg")
width = int(image.shape[1] * 25 / 100)
height = int(image.shape[0] * 25 / 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation=cv2.INTER_NEAREST )
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

_, binary = cv2.threshold(gray, 150, 150, cv2.THRESH_BINARY_INV)

# GRAB EXTERNAL CONTOUR
contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# print(contours)
print(hierarchy)
# hierarchy returns [Next, Previous, First_Child, Parent]

mask = np.ones(image.shape[:2], dtype="uint8") * 255 # white mask

cv2.drawContours(mask, contours, -1, 0, -1)
img = cv2.bitwise_and(gray, gray, mask=mask)

while cv2.waitKey(ord("q")):
	cv2.imshow("Mask", img)

data = np.vstack(contours).squeeze()