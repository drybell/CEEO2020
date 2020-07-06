import cv2
import matplotlib.pyplot as plt
import numpy as np

thresh = 100
# read the image
img = cv2.imread("test-TEST.jpg")
scale_percent = 50 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
image = cv2.resize(img, dim, interpolation=cv2.INTER_NEAREST )
# convert to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
# cv2.imshow("test", gray)
# create a binary thresholded image
_, binary = cv2.threshold(gray, thresh, thresh, cv2.THRESH_BINARY_INV)
# show it
# plt.imshow(binary, cmap="gray")
# plt.show()

# find the contours from the thresholded image
contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
data = np.vstack(contours).squeeze()
np.savetxt("test-test.txt", data, fmt="%d")
# exit()
mask = np.ones(image.shape[:2], dtype="uint8") * 255 # white mask

# Draw the contours on the mask
cv2.drawContours(mask, contours, -1, 0, -1)

# remove the contours from the image and show the resulting images
img = cv2.bitwise_and(gray, gray, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("After", img)
contours = sorted(contours, key=cv2.contourArea, reverse=True) 
# perimeters = [cv2.arcLength(contours[i],True) for i in range(len(contours))]
# listindex=[i for i in range(15) if perimeters[i]>perimeters[0]/2]
# draw all contours

image = cv2.drawContours(image, contours, -1, (0, 0, 0), 2) # 2D array of 3x3 RGB values
# res = cv2.bitwise_and(image, contours)
canny = cv2.Canny(image, 100, 200)
cv2.imwrite("TEST-high.jpg", mask) 
cv2.imwrite("TEST-high-2.jpg", canny) # Need to look up what format canny returns 


# Convert image data to a more readable 2D plot data. 