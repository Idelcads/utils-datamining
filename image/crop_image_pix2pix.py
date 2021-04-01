import cv2, numpy
import os, re

''' program to crop images in sub images. ''' 

inputPathLabel = '/home/pc/Bureau/Test/crop/raw/label/'
inputPathRgb = '/home/pc/Bureau/Test/crop/raw/rgb/'
outputPathLabel = '/home/pc/Bureau/Test/crop/crop/label/'
outputPathRgb = '/home/pc/Bureau/Test/crop/crop/rgb/'
width = 480
heigth = 352
# Position x and y where we will crop the initial image
x=[0,330,640] # designed for images of size 1120x840 and crop images of size 480x352
y=[0,250,488]

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(inputPathLabel))
seq = 1
n=1
for filenameSrc in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(filenameSrc.endswith(".png") or filenameSrc.endswith(".jpg")):
        filelist.remove(filenameSrc)
    else:
        # # create a folder seq for each image
        # seq_num = '{0:04}'.format(seq)
        # os.makedirs(outputPathLabel + 'seq' + str(seq_num), exist_ok=True)
        # os.makedirs(outputPathRgb + 'seq' + str(seq_num), exist_ok=True)

        # read image and create new empty image of size widht x height
        print(filenameSrc)
        name = filenameSrc[:-4]
        imgRGB = cv2.imread(inputPathRgb+ filenameSrc, cv2.IMREAD_UNCHANGED)
        imglabel = cv2.imread(inputPathLabel + filenameSrc, cv2.IMREAD_UNCHANGED)
        try:
            h,w,c = imglabel.shape
        except:
            h,w = imglabel.shape
            c = 0
        new_imgRGB = numpy.zeros(shape=(heigth,width,3), dtype='uint8')
        if c==0:
            new_imglabel = numpy.zeros(shape=(heigth,width), dtype='uint8')
        else:
            new_imglabel = numpy.zeros(shape=(heigth,width,3), dtype='uint8')

        pair=0
        for j in y:
            if pair == 0:
                for i in x:
                    # print(str(i) + '__' + str(j))
                    num = '{0:06}'.format(n)
                    new_imgRGB[:,:,:] = imgRGB[j:j+heigth, i:i+width, 0:3]
                    if c == 0:
                        new_imglabel[:,:] = imglabel[j:j+heigth, i:i+width]
                    else:
                        new_imglabel[:,:,:] = imglabel[j:j+heigth, i:i+width, 0:3]
                    cv2.imwrite(outputPathLabel + str(num) + '.png', new_imglabel)
                    cv2.imwrite(outputPathRgb + str(num) + '.png', new_imgRGB)
                    n += 1
                pair = 1
            else :
                for i in reversed(x):
                    # print(str(i) + '__' + str(j))
                    num = '{0:06}'.format(n)
                    new_imgRGB[:,:,:] = imgRGB[j:j+heigth, i:i+width, 0:3]
                    if c == 0:
                        new_imglabel[:,:] = imglabel[j:j+heigth, i:i+width]
                    else:
                        new_imglabel[:,:,:] = imglabel[j:j+heigth, i:i+width, 0:3]
                    cv2.imwrite(outputPathLabel + str(num) + '.png', new_imglabel)
                    cv2.imwrite(outputPathRgb + str(num) + '.png', new_imgRGB)
                    n += 1
                pair = 0

        # for j, i in zip(reversed(y[:-1]), reversed(x[:-1])):
        #     j = j+100
        #     i = i+100
        #     print(str(i) + '__' + str(j))
        #     num = '{0:06}'.format(n)
        #     new_imgRGB[:,:,:] = imgRGB[j:j+heigth, i:i+width, 0:3]
        #     new_imglabel[:,:,:] = imglabel[j:j+heigth, i:i+width, 0:3]
        #     cv2.imwrite(outputPathLabel + str(num) + '.png', new_imglabel)
        #     cv2.imwrite(outputPathRgb + str(num) + '.png', new_imgRGB)
        #     n += 1
        # num = '{0:06}'.format(n)
        # new_imgRGB[:,:,:] = imgRGB[20:20+heigth, 30:30+width, 0:3]
        # new_imglabel[:,:,:] = imglabel[20:20+heigth, 30:30+width, 0:3]
        # cv2.imwrite(outputPathLabel + str(num) + '.png', new_imglabel)
        # cv2.imwrite(outputPathRgb + str(num) + '.png', new_imgRGB)
        # n +=1
        seq += 1




