import cv2
import numpy


def horizontal_smooth(img1,img2,val_x,length_smooth):
    heigth, width, color = img1.shape
    length = width
    start1, end1 = val_x[0], val_x[0] + width
    start2, end2 = val_x[1], val_x[1] + width
    length = end1 - start2
    val = int(width/2)
    if length_smooth < length:
        start_img2 = (end1-length_smooth)-start2
        New_image1 = numpy.zeros(shape=(heigth,length_smooth,color), dtype='uint8')
        New_image2 = numpy.zeros(shape=(heigth,length_smooth,color), dtype='uint8')
        New_image3 = numpy.zeros(shape=(heigth,length_smooth,color), dtype='uint8')
        New_image1 = img1[:,width-length_smooth:width,:]
        New_image2 = img2[:,start_img2:start_img2+length_smooth,:]
        New_image3 = img2[:,start_img2:start_img2+length_smooth,:]
        interval = 1
        start=0
        end = 1
        for i in range (1,length_smooth+1):
            dst = cv2.addWeighted(New_image1, 1-i/length_smooth , New_image2, i/length_smooth , 0.0)
            New_image3[:,start:end,:] = dst[:,start:end,:]
            start +=interval
            end +=interval
        return New_image3

    else:
        New_image1 = numpy.zeros(shape=(heigth,length,color), dtype='uint8')
        New_image2 = numpy.zeros(shape=(heigth,length,color), dtype='uint8')
        New_image3 = numpy.zeros(shape=(heigth,length,color), dtype='uint8')
        New_image1 = img1[:,width-length:width,:]
        New_image2 = img2[:,0:length,:]
        New_image3 = img2[:,0:length,:]
        interval = int(length/30)
        start=0
        end = int(length/30)
        for i in range (1,31):
            dst = cv2.addWeighted(New_image1, 1-i/30 , New_image2, i/30 , 0.0)
            New_image3[:,start:end,:] = dst[:,start:end,:]
            start +=interval
            end +=interval
        return New_image3

def add_horizontal_images(left,middle,rigth,length_smooth,length_cover):
    heigth_l, width_l, color = left.shape
    heigth_r, width_r, color = rigth.shape
    heigth_m, width_m, color = middle.shape
    new_width = width_l + width_r - length_cover
    New_image = numpy.zeros(shape=(heigth_l,new_width,color), dtype='uint8')
    New_image [:,0:width_l,:] = left[:,:,:]
    if length_smooth < length_cover:
        New_image [:,width_l-width_m:width_l,:] = middle[:,:,:]
        New_image [:,width_l:,:] = rigth[:,length_cover:,:]
    else:
        New_image [:,width_l-width_m:width_l,:] = middle[:,:,:]
        New_image [:,width_l:,:] = rigth[:,width_m:,:]
    return New_image

def vertical_smooth(img1,img2,val_y,length_smooth):
    heigth, width, color = img1.shape
    start1, end1 = val_y[0], val_y[0] + heigth
    start2, end2 = val_y[1], val_y[1] + heigth
    length = end1 - start2
    val = int(heigth/2)
    if length_smooth < length:
        start_img2 = (end1-length_smooth)-start2
        New_image1 = numpy.zeros(shape=(length_smooth,width,color), dtype='uint8')
        New_image2 = numpy.zeros(shape=(length_smooth,width,color), dtype='uint8')
        New_image3 = numpy.zeros(shape=(length_smooth,width,color), dtype='uint8')
        New_image1 = img1[heigth-length_smooth:heigth,:,:]
        New_image2 = img2[start_img2:start_img2+length_smooth,:,:]
        New_image3 = img2[start_img2:start_img2+length_smooth,:,:]
        interval = int(length/20)
        start=0
        end = int(length/20)
        for i in range (1,21):
            dst = cv2.addWeighted(New_image1, 1-i/20 , New_image2, i/20 , 0.0)
            New_image3[start:end,:,:] = dst[start:end,:,:]
            start +=interval
            end +=interval
        return New_image3
    else:
        New_image1 = numpy.zeros(shape=(length,width,color), dtype='uint8')
        New_image2 = numpy.zeros(shape=(length,width,color), dtype='uint8')
        New_image3 = numpy.zeros(shape=(length,width,color), dtype='uint8')
        New_image1 = img1[heigth-length:heigth,:,:]
        New_image2 = img2[0:length,:,:]
        New_image3 = img2[0:length,:,:]
        interval = int(length/20)
        start=0
        end = int(length/20)
        for i in range (1,21):
            dst = cv2.addWeighted(New_image1, 1-i/20 , New_image2, i/20 , 0.0)
            New_image3[start:end,:,:] = dst[start:end,:,:]
            start +=interval
            end +=interval
        return New_image3

def add_vertical_images(up,middle,down,length_smooth,length_cover):
    heigth_u, width_u, color = up.shape
    heigth_d, width_d, color = down.shape
    heigth_m, width_m, color = middle.shape
    new_heigth = heigth_u + heigth_d - length_cover
    New_image = numpy.zeros(shape=(new_heigth,width_u,color), dtype='uint8')
    New_image [0:heigth_u,:,:] = up[:,:,:]
    New_image [(heigth_u-heigth_m):heigth_u,:,:] = middle[:,:,:]
    if length_smooth < length_cover:
        New_image [heigth_u:,:,:] = down[length_cover:,:,:]
    else:
        New_image [heigth_u:,:,:] = down[heigth_m:,:,:]
    return New_image