import cv2
import numpy as np
import os
import re
import sys
from pathlib import Path

'''program to generate video from png images'''

InputPath = '/home/pc/Documents/PathToImage/'
OutputPath = '/home/pc/Documents/PathToSaveVideo/'

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

img_array = []

filelist=sorted_alphanumeric(os.listdir(InputPath))

for filename in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filename.endswith(".png") or filename.endswith(".jpg")):
        filelist.remove(filename)
    else:
        img = cv2.imread(InputPath + filename)
        height, width, layers = img.shape
        size = (width,height)
        img_array.append(img)

codec = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter(OutputPath + '../final6.avi', codec, 25, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()