import cv2
import math

'''program to extract images from a video'''

video = 'video_name'
inputPath = '/home/pc/PathToVideo/' + video + '.mp4'
outputPath = '/home/pc/PathToSaveImages/'
fps = 25

allFrame = True # possibility to not extract all frames

# Opens the Video file
cap= cv2.VideoCapture(inputPath)
i=0
count=0
index = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    nbSecond = math.floor(index / fps)
    if (allFrame):
        
        cv2.imwrite(outputPath + video + '_' + str(i)+'_' + str(nbSecond) + '.png',frame)
        i+=1
    else:
        if (count % 10 == 0): # Change value to change number of frames to extract
            cv2.imwrite(outputPath + video + '_' + str(i)+'_' + str(nbSecond) + '.png',frame)
            i+=1
        count+=1
    index += 1

cap.release()