from PIL import Image
import numpy as np

img = Image.open("mouse.jpg")
arr = np.array(img)

for i in range(img.height//2):
    for j in  range(img.width):
        temp = arr[i,j].copy()
        arr[i,j] = arr[img.height-1-i, j]
        arr[img.height-1-i, j] = temp

im2 = Image.fromarray(arr)
im2.save("yflipped.jpg")