import os
import cv2
import numpy as np
#import tensorflow as tf
import sys
#import PIL
from PIL import Image
import glob
#from PIL import ImageOps
#from shutil import copyfile
#images directory
images_directory = 'C:\\Users\\coaaa2\\Desktop\\dataset ready for trainijg 2000 cl\\resized\\'
new_images_directory = 'C:\\Users\\coaaa2\\Desktop\\new_cropped_2000\\'


os.makedirs(new_images_directory, exist_ok=True)

for filename in glob.glob(images_directory + '*.png'):
    #print(boxes[0][0])
    # Separate RGB arrays
    print(filename)
    im = Image.open(filename)
    R, G, B = im.convert('RGB').split()
    r = R.load()
    g = G.load()
    b = B.load()
    w, h = im.size
    min_x = w
    min_y = h
    max_x = 0
    max_y = 0
    #print(h)
    #print(w)
    xmin=25
    xmax=113
    ymin=15
    ymax=113
    bb_min_x = int(xmin)#int(boxes[0][0][0] * 128) - int((boxes[0][0][2] / 2) * 128)
    bb_max_x = int(xmax)#int(boxes[0][0][0] * 128) + int((boxes[0][0][2] / 2) * 128)
    bb_min_y = int(ymin)#int(boxes[0][0][1] * 127) - int((boxes[0][0][3] / 2) * 127)
    bb_max_y = int(ymax)#int(boxes[0][0][1] * 127) + int((boxes[0][0][3] / 2) * 127)
    for i in range(w):
        for j in range(h):
            if((i > bb_min_x) and (i < bb_max_x) and (j > bb_min_y) and (j < bb_max_y)):
                if(r[i, j] != 0 or g[i, j] != 0 or b[i, j] != 0):
                    if(i < min_x):
                        min_x = i
                    if(i > max_x):
                        max_x = i
                    if(j < min_y):
                        min_y = j
                    if(j > max_y):
                        max_y = j
    #print(min_x)
    #print(max_x)
    #print(min_y)
    #print(max_y)
    padding  = 2
    if(min_x - padding >= 0):
        min_x -= padding
    else:
        min_x = 0
    if(max_x + padding <= w):
        max_x += padding
    else:
        max_x = w
    if(min_y - padding >= 0):
        min_y -= padding
    else:
        min_y = 0
    if(max_y + padding <= h):
        max_y += padding
    else:
        max_y = h
   #xmin = str(min_x)
    #ymin = str(min_y)
    #xmax = str(max_x)
    #ymax = str(max_y)
    
    print(min_x)
    print(max_x)
    print(min_y)
    print(max_y)
    area = (min_x, min_y, max_x, max_y)
    new_filename_image = filename.replace(images_directory,new_images_directory)
    im.crop(area).save(new_filename_image)
    #im.show(save_im)
    
  
    #new_filename = filename.replace(images_directory,new_images_directory)
    #im.write(new_filename)
    
    #print(new_filename_image)
    #copyfile(save_im, new_filename_image)
    #cv2.imwrite(new_images_directory, save_im)
    print(new_filename_image)
    #saved.save(new_filename_image)
    
