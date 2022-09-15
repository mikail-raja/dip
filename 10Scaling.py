import cv2
import numpy as np

img = cv2.imread("flower.jpg")

uph = int(img.shape[0]*2)
upw = int(img.shape[1]*2)

downh = int(img.shape[0]*0.5)
downw = int(img.shape[1]*0.5)


upscaled = cv2.resize(img, (upw, uph), interpolation=cv2.INTER_AREA)
downscaled = cv2.resize(img, (downw, downh), interpolation=cv2.INTER_AREA )

cv2.imwrite("upscaled.jpg", upscaled)
cv2.imwrite("upscaled.jpg", downscaled)
