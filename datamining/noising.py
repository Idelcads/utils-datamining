import skimage
import matplotlib.pyplot as plt
import skimage.io
import os
import re

'''program to add gaussian noise on images'''

InputPath="/home/pc/Documents/PathToImage/" 
OutPath = "/home/pc/Documents/PathToSave/"

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(InputPath))

# For each frame of the video, we split in multiples images
for filename in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filename.endswith(".png") or filename.endswith(".jpg")):
        filelist.remove(filename)
    else:
    	img = skimage.io.imread(InputPath + filename)/255.0

    	gimg = skimage.util.random_noise(img, mode="gaussian", var=0.01)
    	skimage.io.imsave(OutPath + filename[:-4] + ".jpg", gimg) 
    	# skimage.io.imsave(OutPath + filename[:-4] + ".png", gimg) 
