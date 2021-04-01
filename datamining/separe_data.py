import cv2, numpy
import os, re

'''program to separate folder containing x images into n subfolder containing num_file images'''

inputPath = '/home/path_to_folder_containing_label_images/'
OutputPath = '/home/path_where_output_folder_will_be_created/'
Name_outfolder = 'rgb-'
num_file = 400 #number of file by folder

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputPath))
num_img = 0
num_folder = 1
for image in filelist: # filelist[:] makes a copy of filelist.
    if not(image.endswith(".png") or image.endswith(".jpg")):
        filelist.remove(image)
    else:
        os.makedirs(OutputPath + Name_outfolder + str(num_folder), exist_ok=True)
        img = cv2.imread(inputPath + image)
        if num_img < num_file:
            cv2.imwrite(OutputPath + Name_outfolder + str(num_folder) + '/' + image, img)
            num_img +=1
        else:
            num_img = 0
            num_folder +=1
            os.makedirs(OutputPath + Name_outfolder + str(num_folder), exist_ok=True)
            cv2.imwrite(OutputPath + Name_outfolder + str(num_folder) + '/' + image, img)
            num_img +=1
