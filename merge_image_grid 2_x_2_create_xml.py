import os 
import random
from PIL import Image

NUM_PIC = 2
UNIT_SIZE = 128 # the size of image
UNIT_HEIGH =127 
def merge(images,num):
    target = Image.new('RGB', (UNIT_SIZE*NUM_PIC, UNIT_HEIGH*(NUM_PIC+1)))   # result is 2*2
    for i in range(len(images)):
        if(i%NUM_PIC==0):
            if(i==0):
                left = 0
                lefthight = 0
                right = UNIT_SIZE
                righthight = UNIT_HEIGH
            else:
                left = 0
                lefthight = lefthight + UNIT_HEIGH
                right = UNIT_SIZE
                righthight = righthight + UNIT_HEIGH
            target.paste(images[i], (left, lefthight, right, righthight))
            left += UNIT_SIZE 
            right += UNIT_SIZE 
        else:
            target.paste(images[i], (left, lefthight, right, righthight))
            left += UNIT_SIZE 
            right += UNIT_SIZE 
    gap = Image.new('RGB',(UNIT_SIZE*NUM_PIC,UNIT_HEIGH))
    target.paste(gap,(0,UNIT_HEIGH*NUM_PIC,UNIT_SIZE*NUM_PIC,UNIT_HEIGH*NUM_PIC+UNIT_HEIGH))
    quality_value = 100
    target.save('result6.jpg', quality = quality_value)

rootdir = os.listdir('C:/Users/coaaa2/Desktop/exaple1/')
picSize = NUM_PIC
randlist = []
for i in range(picSize * picSize):
    tmp = random.randint(1,len(rootdir))
    randlist.append(rootdir[tmp])
    
    

path = 'C:/Users/coaaa2/Desktop/exaple1/'
num = NUM_PIC * NUM_PIC
images = []
for i in range(num):
    images.append(Image.open(path+randlist[i])) 
print(randlist)
#myList = randlist
#myList = [i.split('.')[0] for i in myList]
print([i.split('.')[0] for i in randlist])
merge(images,num)


#################################################################################################
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
    
    
#first box
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
    
    text6 = doc.createTextNode([i.split('.')[0] for i in randlist][0]) #name
    text7 = doc.createTextNode('Unspecified') #pose
    text8 = doc.createTextNode('0') #truncated
    text9 = doc.createTextNode('0') #difficult
    text10 = doc.createTextNode('32') #xmin
    text11 = doc.createTextNode('25') #ymin
    text12 = doc.createTextNode('105') #xmax
    text13 = doc.createTextNode('106') #ymax
    
    name.appendChild(text6)
    pose.appendChild(text7)
    truncated.appendChild(text8)
    difficult.appendChild(text9)
    xmin.appendChild(text10)
    ymin.appendChild(text11)
    xmax.appendChild(text12)
    ymax.appendChild(text13)
    
#second box
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
    
    text16 = doc.createTextNode([i.split('.')[0] for i in randlist][1]) #name
    text17 = doc.createTextNode('Unspecified') #pose
    text18 = doc.createTextNode('0') #truncated
    text19 = doc.createTextNode('0') #difficult
    text20 = doc.createTextNode('164') #xmin
    text21 = doc.createTextNode('28') #ymin
    text22 = doc.createTextNode('229') #xmax
    text23 = doc.createTextNode('101') #ymax
    
    name.appendChild(text16)
    pose.appendChild(text17)
    truncated.appendChild(text18)
    difficult.appendChild(text19)
    xmin.appendChild(text20)
    ymin.appendChild(text21)
    xmax.appendChild(text22)
    ymax.appendChild(text23)
    
#third box
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
    text26 = doc.createTextNode([i.split('.')[0] for i in randlist][2]) #name
    text27 = doc.createTextNode('Unspecified') #pose
    text28 = doc.createTextNode('0') #truncated
    text29 = doc.createTextNode('0') #difficult
    text30 = doc.createTextNode('34') #xmin
    text31 = doc.createTextNode('156') #ymin
    text32 = doc.createTextNode('102') #xmax
    text33 = doc.createTextNode('230') #ymax
    
    name.appendChild(text26)
    pose.appendChild(text27)
    truncated.appendChild(text28)
    difficult.appendChild(text29)
    xmin.appendChild(text30)
    ymin.appendChild(text31)
    xmax.appendChild(text32)
    ymax.appendChild(text33)
    
#fourth box
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
    text36 = doc.createTextNode([i.split('.')[0] for i in randlist][3]) #name
    text37 = doc.createTextNode('Unspecified') #pose
    text38 = doc.createTextNode('0') #truncated
    text39 = doc.createTextNode('0') #difficult
    text40 = doc.createTextNode('160') #xmin
    text41 = doc.createTextNode('151') #ymin
    text42 = doc.createTextNode('230') #xmax
    text43 = doc.createTextNode('231') #ymax
    
    
    name.appendChild(text36)
    pose.appendChild(text37)
    truncated.appendChild(text38)
    difficult.appendChild(text39)
    xmin.appendChild(text40)
    ymin.appendChild(text41)
    xmax.appendChild(text42)
    ymax.appendChild(text43)

 
    with open(tTmp,'wb+') as f:
        f.write(doc.toprettyxml(indent='\t',encoding='utf-8'))

    return

if __name__ == '__main__':
    images='C:/Users/coaaa2/Desktop/result6.jpg'
    writeInfoToxml(images)
