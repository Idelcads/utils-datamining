from os import listdir
import cv2
import numpy as np
import os
import re

'''program to copy a list of images'''

path = '/home/path_to_folder_containing_images_to_copy/'
Outpath = '/home/outputpath/'

#name of the images to copy
list_img = [1,4,6,9,12,14,17,20,22,25,28,30,33,36,39,41,44,46,50,52,54,56,58,62,64,65,66,68,70,
	74,76,78,80,84,86,88,92,94,96,98,100,102,104,108,110,114,116,122,124,130,133,139,141,
	147,149,152,153,155,162,163,167,168,176,178,181,184,191,192,196,199,206,209,216,221,
	223,227,229,237,240,245,247,249,253,257,259,262,263,267,268,272,277,278,287,292,295,
	304,306,307,312,313,317,318,343,358,359,365,366,375,396,412,430,619,624,627,629]

for i in range(len(list_img)): # filelist[:] makes a copy of filelist.
    name_img = 'Assemblee-' + str(list_img[i]) + '.png'
    print(name_img)
    img = cv2.imread(path + name_img, cv2.IMREAD_UNCHANGED)
    cv2.imwrite(Outpath + name_img,img)
