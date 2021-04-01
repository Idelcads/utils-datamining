import cv2, numpy
import os, re
''' program to find all x and y positions of a color in a label image and apply processing at this position on another images'''
inputimg = '/home/input_path_to_folder_containing_images_to_process/'
namelabel = '/home/path_to_label/name_label.png'
outputPath1 = '/home/outputpaht_to_save_processed_images/'
width = 1920
heigth = 1080

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputimg))

n=0
imglabel = cv2.imread(namelabel, cv2.IMREAD_UNCHANGED)
## récupération des images RGB fond vert et gray fond vert 
for filenameSrc in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filenameSrc.endswith(".png") or filenameSrc.endswith(".jpg")):
        filelist.remove(filenameSrc)
    else:
        #print(filenameSrc)
        imgRGB = cv2.imread(inputimg + filenameSrc, cv2.IMREAD_UNCHANGED)
        new_image = cv2.imread(inputimg + filenameSrc, cv2.IMREAD_UNCHANGED)

## Extraction of the label of interest on the RGB image
        height, width = imgRGB.shape[:2]

        val = [255,255,255]
        test = imglabel[:,:,0:3]
        index_v = numpy.where(test==val)
        new_image[index_v[0],index_v[1]] = [0,0,0]
        
        # On enregistre l'images dans le nouveau dossier
        cv2.imwrite(outputPath1 +  filenameSrc, new_image)
        n +=1
        print(n)



