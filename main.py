
from detection import get_gesture_in_each_frame
from buffer import draw_marker, init_buffer
import cv2


if __name__ == '__main__':
    video = cv2.VideoCapture(0)
    init_buffer(video)

    while True:
        ret, frame = video.read()
        gesture = get_gesture_in_each_frame(video)

        frame = draw_marker(ret, frame, gesture)

        if cv2.waitKey(1) == ord('q'):
            break
        cv2.imshow("Output", frame)

    video.release()

    cv2.destroyAllWindows()
