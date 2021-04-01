from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img, save_img
from  scipy import ndimage
import os, re

def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

data_gen_args = dict(rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='constant',
        cval = 0)

imageHD_datagen = ImageDataGenerator(**data_gen_args)
imageLD_datagen = ImageDataGenerator(**data_gen_args)

SRCPathHD = 'D:/Datasets/FACESEG/HD/'
SRCPathLD = 'D:/Datasets/FACESEG/label/'
HDPath = 'D:/Datasets/FACESEG/train_img/'
LDPath = 'D:/Datasets/FACESEG/train_label/'


filelist=sorted_alphanumeric(os.listdir(SRCPathHD))

# For each frame of the video, we split in multiples images
for inputImg in filelist[:]: # filelist[:] makes a copy of filelist.

        print(inputImg)

        # HD
        imgHD = load_img(SRCPathHD + inputImg)  # this is a PIL image
        xHD = img_to_array(imgHD)  # this is a Numpy array with shape (3, 150, 150)
        xHD = xHD.reshape((1,) + xHD.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

        # LD
        imgLD = load_img(SRCPathLD + inputImg)  # this is a PIL image
        xLD = img_to_array(imgLD)  # this is a Numpy array with shape (3, 150, 150)
        xLD = xLD.reshape((1,) + xLD.shape)  # this is a Numpy array with shape (1, 3, 150, 150)


        # the .flow() command below generates batches of randomly transformed images
        # and saves the results to the `preview/` directory
        i = 0

        seed = 1

        for i in range(100):
                generatorHD = imageHD_datagen.flow(xHD, batch_size=1,
                                        save_to_dir=HDPath, save_prefix=inputImg[:-4], save_format='png', seed=seed)

                generatorLD = imageLD_datagen.flow(xLD, batch_size=1,
                                        save_to_dir=LDPath, save_prefix=inputImg[:-4], save_format='png', seed=seed)

                generatorHD.next()
                generatorLD.next()
                seed += 1