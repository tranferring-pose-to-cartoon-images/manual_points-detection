# manual points detector
# Friday June 1, 2019
# Ali Raza


import argparse
import cv2
 

# Will hold the points being clicked on the image
refPt = []

 
def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global refPt
 
	
	if event == cv2.EVENT_LBUTTONUP:
	
		refPt.append((x, y))
		cv2.circle(image, refPt[-1], 2, (0,255,0), thickness=2, lineType=8, shift=0)
		cv2.imshow("image", image)
		
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
 
# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)
 
# keep looping until the 'q' key is pressed
while True:
	# display the image and wait for a keypress
	cv2.imshow("image", image)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'r' key is pressed, reset the image
	if key == ord("r"):
		image = clone.copy()
		refPt = []
 
	# if the 'q' key is pressed, break from the loop
	elif key == ord("q"):
		print('Points Detected: ', len(refPt) )
		print(refPt)
		break
		#return refPt
 