import cv2
import numpy as np

img = cv2.imread("flower.jpg")

height, width = img.shape[:2]
transmat = np.float32( [ 
        [1, 0, height//5], 
        [0, 1, width//5] 
        ])

img_translated = cv2.warpAffine(img, transmat, (width, height))
cv2.imwrite("translation.jpg", img_translated)
