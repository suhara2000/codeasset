import cv2
import numpy as np

img=cv2.imread("886737.jpg")
img=cv2.resize(img, (300,300))
height, width, channels = img.shape

print(height,width,channels)

for x in range(0,width):
    for y in range(0,height):
        if img[x,y,0] == 255 and img[x,y,1] == 255 and img[x,y,2] == 255:            
            img[x,y,0] = 0
            img[x,y,1] = 0
            img[x,y,2] = 0

        elif img[x,y,0] == 0 and img[x,y,1] == 0 and img[x,y,2] == 0:
            img[x,y,0] = 255
            img[x,y,1] = 255
            img[x,y,2] = 255

cv2.imshow('asd',img)
cv2.waitKey(0)
cv2.destroyAllWindows()