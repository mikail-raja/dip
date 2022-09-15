# # from PIL import Image

# # img = Image.open("flower.jpg")
# # img_data = img.getdata()

# # lst=[]

# # for i in img_data:
# #     lst.append(i[0]*0.299+i[1]*0.587+i[2]*0.114)

# # new_img = Image.new("L", img.size)
# # new_img.putdata(lst)

# # new_img.save("bw.jpg")


from PIL import Image
import numpy as np
img = Image.open("flower.jpg")
arr = np.zeros(img.height*img.width)
data = np.array(img)
count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        arr[count] = data[i,j,0] * 0.299 + data[i,j,1] * 0.587 + data[i,j,2] * 0.144; count+=1

im2 = Image.new(mode="L", size=img.size)
im2.putdata(arr)
im2.save("Monochrome.jpg")