# from PIL import Image

# # Read image
# img = Image.open('flower.jpg')

# # Output Images
# im2 = img.save("flowercopy.jpg")

# # prints format of image
# print(img.format)

# # prints mode of image
# print(img.mode)

from PIL import Image

img = Image.open("flower.jpg")

img2 = img.save("saved.jpg")
