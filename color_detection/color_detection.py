import cv2
import numpy as np


def processFrame(img, lowerRange, upperRange):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(image, lowerRange, upperRange)

    # apply the contours
    contours, hierchy = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    retVal = None
    if len(contours) != 0:
        for contour in contours:
            if cv2.contourArea(contour) > 100:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 0, 255), 3)

                averageX = x + w / 2
                averageY = y + h / 2
                retVal = (int(averageX), int(averageY))
                break
                # return (int(averageX), int(averageY))

    print("masking done")

    cv2.imshow("masked", mask)
    # cv2.imshow("cam", img)
    return retVal
