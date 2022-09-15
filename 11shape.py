import cv2
import numpy as np

img = np.zeros((500,500,3), dtype="uint8")

cv2.line(img, (50,50), (200,50), color=(255,255,255), thickness=5)

cv2.rectangle(img, pt1=(50, 100), pt2=(200, 200), color=(255,255,255), thickness=5)

cv2.circle(img, center=(125,275), radius=50, color=(255,255,255), thickness=5)

cv2.ellipse(img, (225, 350), (50,100), 0, 0, 360, color=(255,255,255), thickness=5)

cv2.putText(img, "Text" ,  (300, 400), cv2.FONT_HERSHEY_PLAIN, 4, color=(255,255,255), thickness=3 )

cv2.imwrite("shapes.jpg", img)

