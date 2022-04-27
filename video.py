import  cv2 as cv

capture = cv.VideoCapture(r'C:\Users\labhk\Videos\dog.mp4')


while True:
    isTrue, f = capture.read()

    cv.imshow("MASSIVE", f)

    if cv.waitKey(30) == ord('d'):
        break


capture.release()
cv.destroyAllWindows()