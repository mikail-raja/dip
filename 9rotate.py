import cv2
import numpy as np

img = cv2.imread("flower.jpg")

height, width = img.shape[:2]
center = (height//2, width//2)

rotatemat = cv2.getRotationMatrix2D(center, angle=-45, scale=0.70)

rotateimg = cv2.warpAffine(img, rotatemat, (width, height) )

cv2.imwrite("rotation.jpg",rotateimg)
