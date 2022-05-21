import cv2 as cv
cap = cv.VideoCapture(0)

while True:
    ret, frame  = cap.read()
    im = cv.cvtColor(frame, cv.COLOR_RGB2RGBA)
    cv.imshow('OpenCv', im)
    if(cv.waitKey(1) & 0xFF == ord('p')):
        break

cap.release()
cv.destroyAllWindows()

