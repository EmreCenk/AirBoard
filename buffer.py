import cv2
import numpy as np
from constants import upperRange, lowerRange
from color_detection.color_detection import processFrame


def init_buffer(cap):
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    drawing_buf = np.zeros((height, width, 4), dtype="uint8")
    return drawing_buf


def draw_marker(drawing_buf, frame, gesture, last_pos):
    print("sjgfwehj")
    marker_pos = None

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

    # Edit drawing buffer
    drawing_coords = processFrame(frame, lowerRange, upperRange)
    if drawing_coords and gesture == "fist":
        # Draw small circle
        marker_pos = drawing_coords

        if last_pos:
            # Draw line from last_pos to marker_pos
            cv2.line(
                img=drawing_buf,
                pt1=last_pos,
                pt2=marker_pos,
                color=(255, 0, 0, 255),
                thickness=5,
            )

    # Convert alpha channel of drawing_buf to a mask
    _, _, _, alpha = cv2.split(drawing_buf)
    mask = cv2.bitwise_not(alpha)
    _, mask = cv2.threshold(mask, 120, 255, cv2.THRESH_BINARY)
    frame = cv2.bitwise_and(frame, frame, mask=mask)

    # Draw buffer on top of frame
    frame += drawing_buf

    # cv2.imshow("b and w", bw)
    if cv2.waitKey(1) == ord("a"):
        cv2.circle(
            img=drawing_buf,
            center=(50, 50),
            radius=20,
            color=(0, 255, 0, 255),
            thickness=10,
        )

    return frame, marker_pos
