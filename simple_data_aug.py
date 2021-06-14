#resize image folder
from PIL import Image
import os, sys

path = "C:/Users/Tony/Documents/AnacondaProjects/tensorflow1/models/research/object_detection/images/test/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((100,100), Image.ANTIALIAS)
            imResize.save(f + ' resized.png', 'PNG', quality=90)

resize()
 ## Or try using this step to change the filename
#resize image folder
from PIL import Image
import os, sys

path ='F:/train/'
outpath='F:/check/size/10/'
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((15,15), Image.ANTIALIAS)
           # imResize = im.resize(( 0,20), Image.ANTIALIAS)
            fullpath = os.path.join(outpath, '15_blur_' + item)
            print(fullpath)
            misc.imsave(fullpath, imResize)
            #imResize.save(f + ' resized.png', 'PNG', quality=90)

resize()



#rotate image folder
from scipy import ndimage, misc
import numpy as np
import os
import cv2

def main():
    outPath = "C:/Users/Tony/Documents/AnacondaProjects/tensorflow1/models/research/object_detection/images/test/"
    path = "C:/Users/Tony/Documents/AnacondaProjects/tensorflow1/models/research/object_detection/images/test/"

    # iterate through the names of contents of the folder
    for image_path in os.listdir(path):

        # create the full input path and read the file
        input_path = os.path.join(path, image_path)
        image_to_rotate = ndimage.imread(input_path)

        # rotate the image
        rotated = ndimage.rotate(image_to_rotate, 120)

        # create full output path, 'example.jpg' 
        # becomes 'rotate_example.jpg', save the file to disk
        fullpath = os.path.join(outPath, 'rotated_'+image_path)
        misc.imsave(fullpath, rotated)

if __name__ == '__main__':
    main()
    
    
    
#cropped images in folder
from PIL import Image
import os.path, sys

path = "C:/Users/Tony/Documents/AnacondaProjects/tensorflow1/models/research/object_detection/New folder/"
dirs = os.listdir(path)

def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((32, 29, 79, 81)) 
            imCrop.save(f + 'Cropped.png', "PNG", quality=100)

crop()

#Blur images in folder by applying guassian blur
from scipy import ndimage, misc
import numpy as np
import os
import cv2
from PIL import Image
from PIL import ImageFilter
import os,sys
path ='F:/check/'
outpath='F:/check/ch/'
dirs = os.listdir(path)
def resolution():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f,e = os.path.splitext(path+item)
            im2 = im.filter(ImageFilter.GaussianBlur(0.5))
            fullpath = os.path.join(outpath, 'blur_' + item)
            misc.imsave(fullpath, im2)
            #im2.save( (f + '.png').format(blur), 'PNG', quality =90)
resolution()

#Mirror images in folders
from PIL import Image
import os, sys

path = "C:/Users/Tony/Documents/AnacondaProjects/tensorflow1/models/research/object_detection/New folder/"
dirs = os.listdir( path )

def transpose():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imMirror = im.transpose(Image.FLIP_LEFT_RIGHT)#Image.FLIP_TOP_BOTTOM,Image.TRANSPOSE
            imMirror.save(f + ' transpose.png', 'PNG', quality=90)

transpose()

