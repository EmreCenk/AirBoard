from detection import get_gesture_in_each_frame
from buffer import draw_marker, init_buffer
import cv2


if __name__ == "__main__":
    video = cv2.VideoCapture(0)
    drawing_buf = init_buffer(video)
    last_pos = None

    while True:
        _, frame = video.read()
        frame = cv2.flip(frame, 1)
        # gesture = get_gesture_in_each_frame(video)

        # frame, last_pos = draw_marker(drawing_buf, ret, frame, gesture, last_pos)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        elif key == ord("d"):
            frame, last_pos = draw_marker(drawing_buf, frame, "fist", last_pos)
        elif key == ord("c"):
            drawing_buf.fill(0)
        else:
            frame, last_pos = draw_marker(drawing_buf, frame, "", last_pos)

        cv2.imshow("Output", frame)

    video.release()

    cv2.destroyAllWindows()
