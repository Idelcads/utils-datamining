from os import listdir
import cv2
import numpy as np
import os
import re

'''program to generate segmented images from label images. need to specify the list of input hexadecimal color present in the label images'''

path = '/home/path_to_folder_containing_label_images/'
Outpath = '/home/path_to_segmented_images/'

listL = []

# List of hexadecimal color
hexaList = ['#00ff00', '#000000', '#ff00ff', '#ff0aff', '#ff14ff', '#ff1eff', '#ff28ff', '#ff32ff', '#ff3cff', '#ff46ff', '#ff50ff', '#ff5aff', '#ff64ff', '#ff6eff',
            '#ff78ff', '#ff82ff', '#ff8cff', '#ff96ff', '#ffa0ff', '#ffaaff', '#ffb4ff', '#ffc8ff', '#ffd2ff', '#ffdcff', '#ffe6ff', '#fff0ff', '#ffffff', '#ff1400',
            '#ff2800', '#ff3c00', '#ff5000', '#ff6400', '#ff7800', '#ff8c00', '#ffa000', '#ffffff']

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

def nearestHexa(img, i, j, height, width):
    hexaTmp = []
    for k in range (-1, 2):
        for l in range (-1, 2):
            if (i + k >= 0 and j + l >= 0 and i + k < height and j + l < width):
                color = (img[i + k, j + l])
                hexa = '#{:02x}{:02x}{:02x}'.format(color[0], color[1] , color[2])
                if (hexa in hexaList):
                    hexaTmp.append(hexa)

    if (len(hexaTmp) == 0):
        # Idéalement, calculer un périmètre plus grand (range (-2,3))
        return hexaList[0]
    else:
        return max(hexaTmp,key=hexaTmp.count)

filelist=sorted_alphanumeric(os.listdir(path))

for filenameSrc in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filenameSrc.endswith(".png") or filenameSrc.endswith(".jpg")):
        filelist.remove(filenameSrc)
    else:

        print(filenameSrc)

        imgSrc = cv2.imread(path + filenameSrc, cv2.IMREAD_UNCHANGED)
        height, width, channels = imgSrc.shape
        img = np.zeros((height, width, 3), dtype = "uint8")

        for i in range(height):
            for j in range(width):
                color = (imgSrc[i, j])
                hexa = '#{:02x}{:02x}{:02x}'.format(color[2], color[1] , color[0])
                k = imgSrc[i,j]

                if (hexa not in hexaList):
                    hexa = nearestHexa(imgSrc, i, j, height, width)
                    #img[i, j] = tuple(int(hexa.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

                # listL.append(hexa)                 
                img[i, j] = hexaList.index(hexa)

        cv2.imwrite(Outpath + filenameSrc,img)
