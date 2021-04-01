from PIL import Image
import os, numpy
import re

'''program to generate png image from jpg'''

inputPath = '/home/pc/Documents/PathToImages/'
outputPath = '/home/pc/Documents/PathToSave/'

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputPath))
i = 0
for image in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(image.endswith(".png") or image.endswith(".jpg")):
        filelist.remove(image)
    else:
    	name = image(:-4)
        im1 = Image.open(inputPath + image)
        im1.save(outputPath + name + '.png')
        i+=1