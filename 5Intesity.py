# from PIL import Image
# import numpy as np

# img = Image.open("mouse.jpg")
# hgt = img.height
# wdt = img.width
# img = np.array(img)


# for i in range(hgt):
#     for j in range(wdt):
#         for k in range(3):
#             img[i,j,k] += 40
#             if(img[i,j,k] > 255):
#                 img[i,j,k] = 255


# inverted_img = Image.fromarray(img)
# inverted_img.save(r"Intense.jpg")

from PIL import Image
import numpy as np

img = Image.open("flower.jpg")
arr = np.array(img)

for i in range(img.height):
    for j in range(img.width):
        arr[i,j,0] += 25
        if(arr[i,j,0] > 255): arr[i,j,0] == 255
        arr[i,j,1] += 25
        if(arr[i,j,1] > 255): arr[i,j,1] == 255
        arr[i,j,2] += 25
        if(arr[i,j,2] > 255): arr[i,j,2] == 255

im2 = Image.fromarray(arr)
im2.save("intense.jpg")