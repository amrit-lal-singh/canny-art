import cv2
import numpy as np




frame = cv2.imread('WhatsApp Image 2022-07-03 at 6.38.36 PM.jpeg')
grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#grey = cv2.GaussianBlur(grey, (5, 5), 0)
grey = cv2.fastNlMeansDenoising(grey)
mask = cv2.inRange(grey,190,255)
edges = cv2.Canny(grey, 190, 200)

lines = cv2.HoughLinesP(
    edges, 1, np.pi / 180,  threshold=10,  minLineLength=10, maxLineGap=10)
j = 0
l, b = edges.shape
for x in range(b):
    for y in range(l):

        if edges[y][x] > 190:
            j = (j+1)%2
        if j == 1 and y % 3 == 0:
            edges[y][x] = 125;
for y in range(l):
    for x in range(b):

        if edges[y][x] > 190:
            j = (j+1)%2
        if j == 1 and y % 3 == 0:
            edges[y][x] = 125;


for points in lines:

    x1, y1, x2, y2 = points[0]

    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)




cv2.imshow('edges', frame)
cv2.imshow('idio', edges)
cv2.imshow('kidio', mask)
cv2.imwrite('edges2.png', frame)
cv2.imwrite('lines2.png', edges)
cv2.imwrite('mask2.png', mask)


cv2.waitKey(0) & 0xFF == ord('q')




