#write_xml_file using the actual image size
# code is better used with object types that are single in the image and occupies the image completely
from xml.dom.minidom import Document
from PIL import Image
import cv2
import glob
import os
import os.path as osp

#images = [cv2.imread(file) for file in glob.glob('/home/coaaa2/Downloads/ex/*png')]

def writeInfoToxml(fileN):
#create root
    doc = Document()
    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)

#append folder
    folder = doc.createElement('folder')
    annotation.appendChild(folder)
    text1 = doc.createTextNode('characterset') #folder name
    folder.appendChild(text1)
    
#append filename
    filename = doc.createElement('filename')
    annotation.appendChild(filename)
    tTmp = fileN
    sTmp = tTmp.split('.')
    tTmp = sTmp[0] +'.xml'
    text2 = doc.createTextNode(fileN)   #filename
    filename.appendChild(text2)

#append path
    path = doc.createElement('path')
    annotation.appendChild(path)
    text3 = doc.createTextNode('data/VOCdevkit2007/VOC2007/JPEGImages/'+fileN)  #path
    path.appendChild(text3)
    
    source = doc.createElement('source')
    annotation.appendChild(source)

    database = doc.createElement('database')
    source.appendChild(database)
    text4 = doc.createTextNode('JapaneseDate')  #databasename
    database.appendChild(text4)
    
    size = doc.createElement('size')
    annotation.appendChild(size)
    width = doc.createElement('width')
    heigh = doc.createElement('heigh')
    depth = doc.createElement('depth')
    textW = doc.createTextNode('128')   #text width
    textH = doc.createTextNode('127')   #text heigh
    textD = doc.createTextNode('1')     #text depth
    size.appendChild(width)
    size.appendChild(heigh)
    size.appendChild(depth)
    width.appendChild(textW)
    heigh.appendChild(textH)
    depth.appendChild(textD)
    
    segmented = doc.createElement('segmented')
    annotation.appendChild(segmented)
    text5 = doc.createTextNode('0') #segmented
    segmented.appendChild(text5)
    
    objectT = doc.createElement('object')
    annotation.appendChild(objectT)
    name = doc.createElement('name')
    pose = doc.createElement('pose')
    truncated = doc.createElement('truncated')
    difficult = doc.createElement('diffcult')
    bndbox = doc.createElement('bndbox')
    objectT.appendChild(name)
    objectT.appendChild(pose)
    objectT.appendChild(truncated)
    objectT.appendChild(difficult)
    objectT.appendChild(bndbox)

    xmin = doc.createElement('xmin')
    ymin = doc.createElement('ymin')
    xmax = doc.createElement('xmax')
    ymax = doc.createElement('ymax')

    bndbox.appendChild(xmin)
    bndbox.appendChild(ymin)
    bndbox.appendChild(xmax)
    bndbox.appendChild(ymax)

    text6 = doc.createTextNode(sTmp[0][-4:]) #name
    text7 = doc.createTextNode('Unspecified') #pose
    text8 = doc.createTextNode('0') #truncated
    text9 = doc.createTextNode('0') #difficult
    text10 = doc.createTextNode('25') #xmin
    text11 = doc.createTextNode('15') #ymin
    text12 = doc.createTextNode('110') #xmax
    text13 = doc.createTextNode('110') #ymax

    name.appendChild(text6)
    pose.appendChild(text7)
    truncated.appendChild(text8)
    difficult.appendChild(text9)
    xmin.appendChild(text10)
    ymin.appendChild(text11)
    xmax.appendChild(text12)
    ymax.appendChild(text13)

 
    with open(tTmp,'wb+') as f:
        f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))

    return

if __name__ == '__main__':
   images='ex'
##read folder
   imlist = [osp.join(osp.realpath('.'), images, img) for img in os.listdir(images) if os.path.splitext(img)[1] == '.png']
   print(len(imlist))
   for i in range(len(imlist)):
       print(imlist[i])
       writeInfoToxml(imlist[i])
##('1_4734.png')
##(cv2.imread(file) for file in glob.glob('/home/coaaa2/Downloads/ex/*png'))

