import cv2, numpy
import os, re

'''program to crop part of the image from size a*b to b*b or from size a*b to a'*b' '''
''' already used to crop image from 1920x1080 to 1536x1152 (add of black headband) and from 512x384 to 384x384'''

inputPath1 = '/home/path_to_folder_containing_images/'
outputPath1 = '/home/outputpath/'

width = 1920
heigth = 1080
width_final = 1536
heigth_final = 1152

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputPath1))
for filenameSrc in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filenameSrc.endswith(".png") or filenameSrc.endswith(".jpg")):
        filelist_RGB_face.remove(filenameSrc)
    else:
        # read image and create new empty image of size widht x height
        print(filenameSrc)
        name = filenameSrc[:-4]
        imgRGB = cv2.imread(inputPath1+ filenameSrc, cv2.IMREAD_UNCHANGED)
        new_imgRGB = numpy.zeros(shape=(heigth_final,width_final,3), dtype='uint8')

        delta_heigth = int(abs(heigth - heigth_final))
        delta_width = int(abs(width - width_final)/2)

        new_imgRGB[delta_heigth:,:,:] = imgRGB[:, delta_width:width_final+delta_width, 0:3]

        cv2.imwrite(outputPath1 + filenameSrc, new_imgRGB)
