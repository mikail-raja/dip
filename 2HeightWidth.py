# # import required module
# from PIL import Image

# # get image
# img = Image.open("flower.jpg")

# # get width and height
# width = img.width
# height = img.height

# # display width and height
# print("The height of the image is: ", height)
# print("The width of the image is: ", width)

from PIL import Image
import numpy as np

img = Image.open("mouse.jpg")
print(f"Height = {img.height}, Widht = {img.width}")

img = np.array(img)
print(f"height = {len(img)}, width = {len(img[0])} ")