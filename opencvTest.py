import cv2 as cv

# img = cv.imread('images/im1.png')

# cv.imshow('what', img)

#create a capture variable
# capture = cv.VideoCapture('videos/vid.mp4') #webcam is accessed by 0
capture = cv.VideoCapture(0)

while True:
    #reads this video frame by frame and gives a T or F to say the frame is read or not
    isTrue, frame = capture.read() #read method does ^
    cv.imshow('whatever name', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release() 
cv.destroyAllWindows()