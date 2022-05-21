import cv2
import numpy as np

lowerRange = np.array([100, 100, 89])
upperRange = np.array([115, 255, 255])


def processFrame(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lowerRange, upperRange)

    # apply the contours
    contours, hierchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 0, 255), 3)

                averageX = x + w / 2
                averageY = y + h / 2

                return (int(averageX), int(averageY))

    # cv2.imshow("masked", mask)
    # cv2.imshow("cam", img)
