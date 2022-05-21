import cv2
import numpy as np


cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

drawing_buf = np.zeros((height, width, 4), dtype="uint8")


def mouse_click(event, x, y, flag, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing_buf[x][y] = not drawing_buf[x][y]


while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("error!")
        continue

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2RGBA)

    # Add the drawing buffer to the webcam capture

    # Convert alpha channel of drawing_buf to a mask
    _, _, _, alpha = cv2.split(drawing_buf)
    mask = cv2.bitwise_not(alpha)
    _, mask = cv2.threshold(mask, 120, 255, cv2.THRESH_BINARY)
    frame = cv2.bitwise_and(frame, frame, mask=mask)

    # cv2.imshow("b and w", bw)
    if cv2.waitKey(1) == ord("a"):
        cv2.circle(
            img=drawing_buf,
            center=(50, 50),
            radius=20,
            color=(0, 255, 0, 255),
            thickness=10,
        )

    frame += drawing_buf

    cv2.imshow("Webcam Capture", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()