import random
import cv2
from matplotlib import pyplot as plt
import albumentations as A
import os, re

'''program to generate data-augmentation on images, labels and segmented labels, using no interpolation for labels and segmented labels and other interpolation for images'''

## Parameters
Pathimg = '/home/path_to_folder_containing_images/'
Pathlabel = '/home/path_to_folder_containing_labels/'
Pathseg = '/home/path_to_folder_containing_segmented_labels/'

Outpathimg = '/home/path_to_dataaugmented_images/'
OutPathlabel = '/home/path_to_dataaugmented_labels/'
OutPathseg = '/home/path_to_dataaugmented_segmented_labels/'

zoom_min, zoom_max = 0.9 , 0.95 #0.85, 0.95
num_data = 5 # number of new images to generate for each input

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(Pathimg))

for inputImg in filelist[:]: # filelist[:] makes a copy of filelist.
    if not(inputImg.endswith(".png") or inputImg.endswith(".jpg")):
        filelist.remove(inputImg)
    else:
        print(inputImg)

        image = cv2.imread(Pathimg + inputImg)
        image_seg = cv2.imread(Pathseg + inputImg , cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(Pathlabel + inputImg)

        height, width = image.shape[0], image.shape[1]
        size_zoom = [int(zoom_min*height),int(zoom_max*height)]

        transform = A.ReplayCompose([
                A.HorizontalFlip(p=0.4),
                # A.Rotate(p=0.2, limit=[-40,40], interpolation=cv2.INTER_NEAREST,
                #         border_mode=cv2.BORDER_CONSTANT, value=0, mask_value=0),
                A.RandomSizedCrop(min_max_height=size_zoom, height=height, width=width,
                        p=0, interpolation=cv2.INTER_NEAREST), #p=0.2, interpolation=cv2.INTER_NEAREST),
                A.ShiftScaleRotate(shift_limit=0.2, scale_limit=0, p=0.6, #scale limit : closer than 1 mean more zoom out
                        rotate_limit=[-5,5], interpolation=cv2.INTER_NEAREST,
                        border_mode=cv2.BORDER_CONSTANT, value=0, mask_value=0),
                # A.Perspective(keep_size=True, p=0.2, scale=[0.05,0.1], interpolation=0)
                                   ],
                additional_targets={'image_seg': 'mask'}
                                  )

        i = 0
        for i in range(num_data):
                transformed = transform(image=image, mask=mask, image_seg=image_seg)
                image_transform_nearest = transformed['image']
                mask_transform = transformed['mask']
                image_seg_transform = transformed['image_seg']
                #We apply the same transforms but with linear interpolation on RGB image
                transformed['replay']['transforms'][1]['interpolation']=1
                transformed['replay']['transforms'][2]['interpolation']=1
                # transformed['replay']['transforms'][3]['interpolation']=1
                transformed2 = A.ReplayCompose.replay(transformed['replay'], image=image)
                image_transform_linear = transformed2['image']
                name = inputImg[:-4] + '_' + str(i+1) + '.png'
                cv2.imwrite(OutPathlabel + name, mask_transform)
                cv2.imwrite(OutPathseg + name, image_seg_transform)
                cv2.imwrite(Outpathimg + name, image_transform_linear)
                
