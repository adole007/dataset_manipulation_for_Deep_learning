#this code helps to adjust bounding box coordinate obtained in XML
#the output of th bounding box coordinate can be visualised using LabelImg software
from PIL import Image
import glob
import os
import xml.etree.ElementTree as ET
from shutil import copyfile
import cv2

#images directory
images_directory = 'train'
new_images_directory = 'new_train'


os.makedirs(new_images_directory, exist_ok=True)

for filename in glob.glob(images_directory + '/*.png'):
    filename_xml = filename
    filename_xml = os.path.splitext(filename_xml)[0]+'.xml'
    #print(filename_xml)
    tree = ET.parse(filename_xml)
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
    bb_min_x = int(tree.find('.//xmin').text)
    bb_max_x = int(tree.find('.//xmax').text)
    bb_min_y = int(tree.find('.//ymin').text)
    bb_max_y = int(tree.find('.//ymax').text)
    #print(bb_min_x)
    #print(bb_max_x)
    #print(bb_min_y)
    #print(bb_max_y)

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
    tree.find('.//xmin').text = str(min_x)
    tree.find('.//ymin').text = str(min_y)
    tree.find('.//xmax').text = str(max_x)
    tree.find('.//ymax').text = str(max_y)
    
    new_filename_xml = filename_xml.replace(images_directory,new_images_directory)
    #print(new_filename_xml)
    tree.write(new_filename_xml)
    new_filename_image = filename.replace(images_directory,new_images_directory)
    #print(new_filename_image)
    copyfile(filename, new_filename_image)
    #img = cv2.imread(new_filename_image)
    #cv2.rectangle(img,(min_x,min_y),(max_x,max_y),(0,255,0),2)
    #cv2.imshow("Image", img)
    #cv2.startWindowThread()
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    print(new_filename_image)
