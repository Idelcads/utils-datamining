from PIL import Image 
import os
import cv2

'''program to compress image in jpg format (mean lose of quality)'''

inputPath = '/home/path_to_folder_containing_images/'
outputPath = '/home/outputpath/'

filelist=os.listdir(inputPath)

for image in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(image.endswith(".png") or image.endswith(".jpg")):
        filelist.remove(image)

    # Opens a image in RGB mode 
    im = Image.open(inputPath + image) 
    
    # Shows the image in image viewer 
    im.save(outputPath + image + image[:-4] + '.jpg', quality=5) 
