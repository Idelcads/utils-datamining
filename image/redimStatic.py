import cv2, numpy
import os, re

'''program which take as input a list of images in order to resize them with the same zoom value if test case and with the same output size'''


inputPath = '/home/path_to_folder_containing_images/'
outputPath = '/home/outputpath/'
width = 256
heigth = 256
case = 'test' #'train'  #train case mean each images have maximum zoom as possible and so a different zoom value

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputPath))

index = 0
if case == 'train':
    for image in filelist[:]: # filelist[:] makes a copy of filelist.
        if not(image.endswith(".png") or image.endswith(".jpg")):
            filelist.remove(image)
        else:

            original_image = cv2.imread(inputPath + image, cv2.IMREAD_UNCHANGED)
            original_heigth, original_width = original_image.shape[:2]

            # Resize
            border_v = 0
            border_h = 0
            if (heigth/width) >= (original_heigth/original_width):
                border_v = int((((heigth/width)*original_width)-original_heigth)/2)
            else:
                border_h = int((((width/heigth)*original_heigth)-original_width)/2)
            green = [0,255,0]
            img = cv2.copyMakeBorder(original_image, border_v, border_v, border_h, border_h, cv2.BORDER_CONSTANT, value=green)  
            img = cv2.resize(img, (width, heigth))

            cv2.imwrite(outputPath + str(index) + ".png", img)
            index += 1

elif case == 'test':
    # loop to find the size of the hightest image on y and the size of the widest image on x and then fixe the zoom to apply on all images
    max_heigth,max_width = 0,0
    for image in filelist[:]: # filelist[:] makes a copy of filelist.
        if not(image.endswith(".png") or image.endswith(".jpg")):
            filelist.remove(image)
        else:
            original_image = cv2.imread(inputPath + image, cv2.IMREAD_UNCHANGED)
            original_heigth, original_width = original_image.shape[:2]
            if original_width > max_width:
                max_width = original_width
            if original_heigth > max_heigth:
                max_heigth= original_heigth
    zoom_widht = width/max_width
    zoom_heigth = heigth/max_heigth
    ## maximisation du zoom
    min_zoom = min(zoom_widht,zoom_heigth)
    min_zoom = round(min_zoom,2)
    if round(min_zoom,1)<=min_zoom:
        zoom = min_zoom
    else:
        zoom = round((min_zoom-0.1),1)
    ## minimisation du zoom
    #zoom = int(min(zoom_heigth,zoom_widht))
    print(zoom)
    for image in filelist[:]: # filelist[:] makes a copy of filelist.
        if not(image.endswith(".png") or image.endswith(".jpg")):
            filelist.remove(image)
        else:
            original_image = cv2.imread(inputPath + image, cv2.IMREAD_UNCHANGED)
            original_heigth, original_width = original_image.shape[:2]
            # Resize
            green = [0,255,0]
            img = cv2.resize(original_image, (int(original_width*zoom), int(original_heigth*zoom)))
            h,w = img.shape[:2]
            img_green = (numpy.zeros(shape=(width,heigth,3), dtype=int)) 
            img_green[:] = green
            for a in range(h):
                for b in range(w):
                    img_green[a,b] = img[a,b,0:3]
            #img = cv2.copyMakeBorder(img, 0, heigth, 0, width, cv2.BORDER_CONSTANT, value=green)  
            #img = cv2.resize(img, (width, heigth))

            cv2.imwrite(outputPath + image, img_green)
            cv2.imwrite(outputPath + str(index) + ".png", img_green)
            index += 1
