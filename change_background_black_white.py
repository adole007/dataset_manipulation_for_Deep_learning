import os
import matplotlib.pyplot as plt
from skimage.data import data_dir
from skimage.util import img_as_ubyte
#from skimage import io
#from skimage.morphology import erosion, dilation, opening, closing, white_tophat
#from skimage.morphology import black_tophat, skeletonize, convex_hull_image
#from skimage.morphology import disk
from PIL import Image
import numpy as np

col = Image.open("E:/Users/coaaa2/Music/models-master/research/object_detection/images/23.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
#bw.save("result_bw.png")



orig_phantom = img_as_ubyte((bw))
fig, ax = plt.subplots()
fig, ax2 = plt.subplots()
change_mask = orig_phantom == 0
change_mask[45:50, 75:80] = 1
ax.imshow(orig_phantom, cmap=plt.cm.gray)
ax2.imshow(change_mask, cmap=plt.cm.gray)
#change_mask.save("result_bw.png")
