#Original Code by Daniel Wong (2018)
#Edited by Elizabeth Willer (2019)
#Allows the user to only show certain parts of an image
# based on selected upper and lower HSV values

import cv2
import numpy as np

#Tell the computer to get the pictures from your webcam 
# (this is probably camera number zero).

video = cv2.VideoCapture(0)

if video.isOpened == False:
    print("Video didn't open properly")

def nothing(x):
    pass

#Create the trackbars for getting the upper and 
# lower HSV values and put them in a window called bar
cv2.namedWindow('bars', cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('h lower', 'bars', 0, 255, nothing)
cv2.createTrackbar('s lower', 'bars', 0, 255, nothing)
cv2.createTrackbar('v lower', 'bars', 0, 255, nothing)
cv2.createTrackbar('h upper', 'bars', 0, 255, nothing)
cv2.createTrackbar('s upper', 'bars', 0, 255, nothing)
cv2.createTrackbar('v upper', 'bars', 0, 255, nothing)

while video.isOpened:
    #Get the image from your camera
    _, frame = video.read()
    #Change from RGB to HSV
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Get the colour ranges
    hLower = cv2.getTrackbarPos('h lower', 'bars')
    sLower = cv2.getTrackbarPos('s lower', 'bars')
    vLower = cv2.getTrackbarPos('v lower', 'bars')
    hUpper = cv2.getTrackbarPos('h upper', 'bars')
    sUpper = cv2.getTrackbarPos('s upper', 'bars')
    vUpper = cv2.getTrackbarPos('v upper', 'bars')
    #Create a black and white image which consists of areas which are in the range 
    colourFilteredImage = cv2.inRange(hsvImage, (hLower, sLower, vLower), (hUpper, sUpper, vUpper))
    #Use this as a mask so the original colours show
    originalMasked = cv2.bitwise_and(frame,frame,mask = colourFilteredImage)
    #Display the windows
    cv2.imshow("masked", originalMasked)
    cv2.imshow("original video", frame)
    cv2.imshow("colour filtered image", colourFilteredImage)
    #Wait 25 seconds and if the ‘q’ key is pressed, break the loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
#Release the resources
video.release()
cv2.destroyAllWindows()
