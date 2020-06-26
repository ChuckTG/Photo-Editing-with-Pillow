import torch
import numpy as np
import PIL
from PIL import Image
import matplotlib.pyplot as plt
from PIL import ImageFilter

#load image and convert to numpy
file_path ='data/ant1.jpeg'
img = Image.open(file_path)
img_numpy_orig = np.array(img)
img_pre=img_numpy_orig.copy()

# plt.imshow(img_edges)
# plt.show()

# define are that we want to edit/smooth
vert_end=1009
vert_start=870
horiz_end=644
horiz_start =128

#apply a GaussianBlur filter in the area
edit_region_numpy = img_numpy_orig[vert_start:vert_end,horiz_start:horiz_end,:]
edit_region = Image.fromarray(edit_region_numpy)
edit_region_smoothed = edit_region.filter(ImageFilter.GaussianBlur(radius=1000))

#replace the area we wanted to edit
img_numpy_orig[vert_start:vert_end,horiz_start:horiz_end,:]= edit_region_smoothed

#Gausian Blur a little more in the nearby area
edit_region2= img_numpy_orig[vert_start-20:vert_end+20,:horiz_end+10,:]
edit_region2_pil= Image.fromarray(edit_region2)
edit_region2=edit_region2_pil.filter(ImageFilter.GaussianBlur(radius=3))
edit_region2 = edit_region2.filter(ImageFilter.GaussianBlur(radius=3))

#Replace the last blurred area
img_numpy_edited=img_numpy_orig.copy()
img_numpy_edited[vert_start-20:vert_end+20,:horiz_end+10,:]=edit_region2

#Visualize pre edit and after edit images
f,axarr = plt.subplots(1,2)
f.set_size_inches(100,100)
axarr[0].imshow(img_pre)
axarr[0].set_title('pre edit')
axarr[1].imshow(img_numpy_edited)
axarr[1].set_title('edited')
plt.show()

