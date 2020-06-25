from PIL import ImageGrab
import numpy as np
import cv2
from time import sleep

fps = 15

for counter in range(1000):
	img = ImageGrab.grab(bbox=(100,10,400,780)) #bbox specifies specific region (bbox= x,y,width,height)
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
	cv2.imshow("test", frame)
	x = cv2.waitKey(fps)
	if x == "q":
		break
cv2.destroyAllWindows()