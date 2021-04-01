import random
import cv2
from matplotlib import pyplot as plt
import albumentations as A
import os, re

'''program to resize images and labels using no interpolation for labels and other interpolation for images'''

## Parameters
Pathimg = '/home/path_to_folder_containing_images/'
Pathmask = '/home/path_to_folder_containing_labels/'

Outpathimg = '/home/path_to_resized_images/'
Outpathmask = '/home/path_to_resized_labels/'

new_width = 512 # []
new_height = 384 # []



def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(Pathimg))

for inputImg in filelist[:]: # filelist[:] makes a copy of filelist.

        print(inputImg)

        image = cv2.imread(Pathimg + inputImg)
        mask_gray = cv2.imread(Pathmask + inputImg , cv2.IMREAD_GRAYSCALE)
        mask = cv2.imread(Pathmask + inputImg)

        height, width = image.shape[0], image.shape[1]

        if not new_width:
                new_width = width
                new_height = height

        transform = A.ReplayCompose([
                A.Resize (new_height, new_width, interpolation=0, always_apply=True)],
                additional_targets={'mask_gray': 'mask'})

        i = 0
        for i in range(1):
                transformed = transform(image=image, mask=mask, mask_gray=mask_gray)
                image_transform_nearest = transformed['image']
                mask_transform = transformed['mask']
                mask_gray_transform = transformed['mask_gray']
                #We apply the same transforms but with linear interpolation on RGB image
                transformed['replay']['transforms'][0]['interpolation']=3 # cv2.INTER_NEAREST, cv2.INTER_LINEAR, cv2.INTER_CUBIC, cv2.INTER_AREA, cv2.INTER_LANCZOS4. Default: cv2.INTER_LINEAR.
                transformed2 = A.ReplayCompose.replay(transformed['replay'], image=image)
                image_transform_linear = transformed2['image']
                name = inputImg
                cv2.imwrite(Outpathmask + name, mask_transform)
                cv2.imwrite(Outpathimg + name, image_transform_linear)
                
