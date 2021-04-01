import cv2, numpy
import os, re

'''program to compare two folder containing jpg or png images'''

inputPath1 = '/home/pc/Documents/PathToImage_1/'
inputPath2 = '/home/pc/Documents/PathToImage_2/'

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)


filelist1=sorted_alphanumeric(os.listdir(inputPath1))
filelist2=sorted_alphanumeric(os.listdir(inputPath2))

# delete names other than .png or .jpg in the list
for image in filelist1[:]: # filelist[:] makes a copy of filelist.
    if not(image.endswith(".png") or image.endswith(".jpg")):
        filelist1.remove(image)
for image in filelist2[:]: # filelist[:] makes a copy of filelist.
    if not(image.endswith(".png") or image.endswith(".jpg")):
        filelist1.remove(image)


missing = []

l=len(filelist2)
index = 0
for j in range(l): # filelist[:] makes a copy of filelist.
    image_rgb = filelist2[j]
    if not os.path.isfile(inputPath1 + image_rgb):
    	missing.append(image_rgb)

l=len(filelist1)
index = 0
for j in range(l): # filelist[:] makes a copy of filelist.
    image_rgb = filelist1[j]
    if not os.path.isfile(inputPath2 + image_rgb):
        missing.append(image_rgb)
print('missing files are: ')
print(missing)
