from PIL import Image
import numpy as np

img = Image.open("mouse.jpg")

arr = np.array(img)
arr2 = arr

for i in range(img.height):
    for j in range(img.width//2):
        temp = arr[i,j].copy()
        arr[i,j] =  arr[i,img.width - 1 - j] 
        arr[i,img.width - 1 - j] = temp

img2 = Image.fromarray(arr2)
img2.save("xflipped.jpg")
