import cv2, numpy
import os, re, csv
''' program which take name of images in a folder (inputpath1) and copy this list of images from another folder (inputpath2) in outputPath'''
inputpath1 = '/home/path_to_folder_containing_images_for_name/' #name of images to copy
inputpath2 = '/home/path_to_folder_containing_images_to_copy/' #images to copy

outputPath = '/home/outputpath/'


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputpath1))


## récupération des images RGB fond vert et gray fond vert 
for filenameSrc in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filenameSrc.endswith(".png") or filenameSrc.endswith(".jpg")):
        filelist.remove(filenameSrc)
    else:
        #print(filenameSrc)
        img = cv2.imread(inputpath2 + filenameSrc, cv2.IMREAD_UNCHANGED)

        cv2.imwrite(outputPath + filenameSrc, img)

        print(filenameSrc)
