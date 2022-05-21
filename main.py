from detection import get_gesture_in_each_frame
from color_detection.color_detection import processFrame

import cv2
import numpy as np

lowerRange = np.array([100, 100, 89])
upperRange = np.array([115, 255, 255])

if __name__ == '__main__':
    video = cv2.VideoCapture(0)


    while True:
        ret, frame = video.read()
        print(processFrame(frame, lowerRange, upperRange))
        print(get_gesture_in_each_frame(video))
        if cv2.waitKey(1) == ord('q'):
            break

    video.release()

    cv2.destroyAllWindows()
