# Improting Image class from PIL module 
from PIL import Image 
import os
import cv2

inputPath = 'C:/Users/crena/Documents/Datasets/BOXE/POC2/Resize/'
outputPath = 'C:/Users/crena/Documents/Datasets/BOXE/POC2/LR/'

filelist=os.listdir(inputPath)

for image in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(image.endswith(".png") and image.endswith(".jpg")):
        filelist.remove(image)

    # Opens a image in RGB mode 
    im = Image.open(inputPath + image) 
    
    # Size of the image in pixels (size of orginal image) 
    # (This is not mandatory) 
    width, height = im.size 

    # Setting the points for cropped image 
    left = (480 - 480) / 2
    top = (278 - 270) / 2
    right = left + 480
    bottom = top + 270

    # Cropped image of above dimension 
    # (It will not change orginal image) 
    im1 = im.crop((left, top, right, bottom)) 
    
    # Shows the image in image viewer 
    im1.save(outputPath + image) 

