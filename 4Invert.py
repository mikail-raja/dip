# from PIL import Image
# import numpy as np

# img = Image.open("1flower.jpg")
# img_arry = np.array(img)

# img_arry = 255 - img_arry

# inverted_img = Image.fromarray(img_arry)
# inverted_img.save("inverted.jpg")

from PIL import Image
import numpy as np

img = Image.open("flower.jpg")
arr = np.array(img)

arr = 255 - arr

inv = Image.fromarray(arr)
inv.save("inv.jpg")