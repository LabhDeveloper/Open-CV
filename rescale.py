import  cv2 as cv

# img = cv.imread(r'C:\Users\labhk\OneDrive\Pictures/scene.jpg')
# #large image

# cv.imshow('RED MOUNTAIN', img)

def rescale(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation= cv.INTER_AREA)


# re_img = rescale(img,0.5)
# cv.imshow('RE image',re_img)
# cv.waitKey(10000)

capture = cv.VideoCapture(r'C:\Users\labhk\Videos\dog.mp4')

while True:
    isTrue, f = capture.read()

    rf = rescale(f,0.2)
    cv.imshow("large", f)
    cv.imshow("small",rf)

    if cv.waitKey(30) == ord('d'):
        break

capture.release()
cv.destroyAllWindows()