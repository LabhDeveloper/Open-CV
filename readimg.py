import  cv2 as cv

img = cv.imread(r'C:\Users\labhk\OneDrive\Pictures/bird.jpeg')

cv.imshow('SEA EAGLE', img)

cv.waitKey(10000)
