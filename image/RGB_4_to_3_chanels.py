import cv2
import os, numpy, re

'''program to remove the 4th chanel from an image'''

inputPath = '/home/pc/Documents/PathToImages/'

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputPath))


for image in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(image.endswith(".png") or image.endswith(".jpg")):
        filelist.remove(image)
    else:

        image_4 = cv2.imread(inputPath + image, cv2.IMREAD_UNCHANGED)
        image_3 = image_4[:,:,0:3]

        cv2.imwrite(inputPath + image, image_3)
