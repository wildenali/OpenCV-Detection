import cv2
import numpy as np

filename = 'chessboard1.png'
# filename = 'chessboard2.png'
# filename = 'chessboard3.jpg'
# filename = 'chessboard4.png'
# filename = 'chessboardA.png'
# filename = 'chessboardB.png'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dilated for making the corners, not important
dst = cv2.dilate(dst, None)

# threshold for an optimal value, it may vary depending on the image
img[dst > 0.01*dst.max()] = [0, 0, 255]

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
