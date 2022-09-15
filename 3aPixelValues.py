# from PIL import Image
# # import numpy as np

# img = Image.open("flower.jpg")
# lst = list(img.getdata())

# print(type(img.getdata()))
# print(type(lst[0][0]))
# print(lst[0][0], lst[0][1], lst[0][2])

# data = img.load()
# print(type(data))
# print(type(data[0,0]))
# print(data[0,0])

from PIL import Image
import numpy as np

img = np.array(Image.open("flower.jpg"))

c=0
for i in range(len(img)):
    for j in range(len(img[0])):
        print(f"Red : {img[i,j,0]} Green : {img[i,j,1]} Yellow : {img[i,j,2]}, counter : {c}")
        c+=1