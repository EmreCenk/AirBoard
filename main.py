from detection import get_gesture_in_each_frame
from color_detection.color_detection import processFrame

import cv2
import numpy as np

# color detection stuff
lowerRange = np.array([100, 100, 89])
upperRange = np.array([115, 255, 255])

video = cv2.VideoCapture(0)


for gesture in get_gesture_in_each_frame():
    print(gesture)

# loop

# for the color detection, processFrame() is only doing one frame, so this needs to be repeated in a loop
# call processFrame for color detection
