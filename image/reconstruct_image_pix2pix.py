import cv2, numpy
import os, re
from reconstruct_image_pix2pix_functions import add_horizontal_images, horizontal_smooth, vertical_smooth, add_vertical_images
import matplotlib.pyplot as plt

''' program to reconstruct images from croped images with smoothing. ''' 
'''Need to define the number of images to reconstruct, the number of crop images to use for 1 images and the position x and y where croped images where crop'''

inputPath1 = '/home/pc/Bureau/Test/crop/crop/rgb/'
outputPath1 = '/home/pc/Bureau/Test/crop/reconstruct/rgb/'
width = 480
heigth = 352
num_imgs = 1 #number of images to reconstruct
num_crop = 9 #number of images used to reconstruct the final image
# x and y are the position where the initial image was cut
x=[0,330,640] # designed for images of size 1120x840 and crop images of size 480x352
y=[0,250,488]
length_smooth = 80 # The pixel band width where to apply the smoothing
pair=0

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputPath1))
for filenameSrc in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filenameSrc.endswith(".png") or filenameSrc.endswith(".jpg")):
        filelist.remove(filenameSrc)

# Je sépare ma liste de num_imgs*num_crop images en sous-listes de num_crop images
n=0
nn=0
filelistSeq = []
for l in range(0,num_imgs):
    filelistImg = []
    n = nn
    for j in y:
        for i in x:
            name_img = filelist[n]
            n+=1
            filelistImg.append(name_img)
    filelistSeq.append(filelistImg)
    nn += num_crop

## Je sépare ma liste de 9 images en sous-liste de 3 images puis j'applique le smooth horizontal
os.makedirs(outputPath1 + 'horizontal/', exist_ok=True)
final_name=0
for listnames in filelistSeq:
    n=0
    nn = 0
    pair=0
    nb_iter = len(y)
    l = int(len(listnames)/nb_iter)
    for j in range(0,l):
        list_lign = []
        for k in range(0,nb_iter):
            if n<len(listnames):
                list_lign.append(listnames[n])
            else:
                print('&')
            n+=1
        print(list_lign)
        ## Pour chaque pack 3 images j'effectue horizontal smoothing + add
        if pair == 0:
            New_line = numpy.array([])
            for i in range(len(list_lign)-1):
                name_img_left = list_lign[i]
                name_img_right = list_lign[i+1]
                img_left = cv2.imread(inputPath1 + name_img_left, cv2.IMREAD_UNCHANGED)
                img_right = cv2.imread(inputPath1 + name_img_right, cv2.IMREAD_UNCHANGED)
                val_x, val_y = [x[i],x[i+1]],[y[i],y[i+1]]
                #
                heigth, width, color = img_left.shape
                start1, end1, start2, end2 = val_x[0], val_x[0] + width, val_x[1], val_x[1] + width
                length_cover = end1 - start2
                #
                middle = horizontal_smooth(img_left,img_right,val_x,length_smooth)
                cv2.imwrite(outputPath1 + 'horizontal/' + str(nn) + '.png', middle)
                if New_line.size==0:
                    New_line = img_left
                    New_line = add_horizontal_images(New_line,middle,img_right,length_smooth,length_cover)
                else:
                    New_line = add_horizontal_images(New_line,middle,img_right,length_smooth,length_cover)
            cv2.imwrite(outputPath1 + 'horizontal/' + str(nn) + '.png', New_line)
            nn+=1
            pair = 1
        else:
            New_line = numpy.array([])
            list_lign=list(reversed(list_lign))
            for i in range(len(list_lign)-1):
                name_img_left = list_lign[i]
                name_img_right = list_lign[i+1]
                val_x, val_y = [x[i],x[i+1]],[y[i],y[i+1]]
                img_left = cv2.imread(inputPath1 + name_img_left, cv2.IMREAD_UNCHANGED)
                img_right = cv2.imread(inputPath1 + name_img_right, cv2.IMREAD_UNCHANGED)
                #
                heigth, width, color = img_left.shape
                start1, end1, start2, end2 = val_x[0], val_x[0] + width, val_x[1], val_x[1] + width
                length_cover = end1 - start2
                #
                middle = horizontal_smooth(img_left,img_right,val_x,length_smooth)
                if New_line.size==0:
                    New_line = img_left
                    New_line = add_horizontal_images(New_line,middle,img_right,length_smooth,length_cover)
                else:
                    New_line = add_horizontal_images(New_line,middle,img_right,length_smooth,length_cover)
            cv2.imwrite(outputPath1 + 'horizontal/' + str(nn) + '.png', New_line)
            nn+=1
            pair = 0
        k+=1
    ## Avec les lignes générés je fais un vertical smoothing
    filelistVer = sorted_alphanumeric(os.listdir(outputPath1 + 'horizontal/'))
    for filename in filelistVer[:]: # filelist[:] makes a copy of filelist.
        if not(filename.endswith(".png") or filename.endswith(".jpg")):
            filelistVer.remove(filename)
    final_image = numpy.array([])
    for p in range(len(filelistVer)-1):
        name_img_up = filelistVer[p]
        name_img_down = filelistVer[p+1]
        img_up = cv2.imread(outputPath1 + 'horizontal/' + name_img_up, cv2.IMREAD_UNCHANGED)
        img_down = cv2.imread(outputPath1 + 'horizontal/' + name_img_down, cv2.IMREAD_UNCHANGED)
        val_x, val_y = [x[p],x[p+1]],[y[p],y[p+1]]
        heigth, width, color = img_left.shape
        start1, end1, start2, end2 = val_y[0], val_y[0] + heigth, val_y[1], val_y[1] + heigth
        length_cover = end1 - start2
        middle = vertical_smooth(img_up,img_down,val_y,length_smooth)
        # cv2.imwrite(outputPath1 + 'vertical/' + 'middle' + str(p) + '.png', middle)
        if final_image.size==0:
            final_image = img_up
            final_image = add_vertical_images(final_image,middle,img_down,length_smooth,length_cover)
            # cv2.imwrite(outputPath1 + 'vertical/' + 'final' + str(p) + '.png', final_image)
        else:
            final_image = add_vertical_images(final_image,middle,img_down,length_smooth,length_cover)
            # cv2.imwrite(outputPath1 + 'vertical/' + 'final' + str(p) + '.png', final_image)
    cv2.imwrite(outputPath1 + str(final_name) + '.png', final_image)
    final_name +=1

## remove horizontal/ directories
import shutil
shutil.rmtree(outputPath1 + 'horizontal/')
               