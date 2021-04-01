import cv2, numpy
import os, re

'''program to generate a list of hexadecimal color from a list of rgb color'''


def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb
    
line_color_alphaPose = [(255, 0, 255),(255, 10, 255), (255, 20, 255), (255, 30, 255), (255, 40, 255),
                (255, 50, 255),(255, 60, 255),(255, 70, 255),(255, 80, 255),(255, 90, 255),
                (255, 100, 255),(255, 110, 255),(255, 120, 255),(255, 130, 255),(255, 140, 255),
                (255, 150, 255),(255, 160, 255),(255, 170, 255),(255, 180, 255), 
                (255, 200, 255),(255, 210, 255),(255, 220, 255),(255, 230, 255),(255, 240, 255),
                (255, 255, 255), #Face
                (255,20,0),(255,40,0),(255,60,0),(255,80,0),#LeftHand
                (255,100,0),(255,120,0),(255,140,0),(255,160,0)]#RightHand


black = (0,0,0)
green = (0,255,0)
white = (255,255,255)

hexa = []

hexa.append(rgb_to_hex(green))
hexa.append(rgb_to_hex(black))
for color in line_color_alphaPose:
     hexa.append(rgb_to_hex(color))
hexa.append(rgb_to_hex(white))
print(len(hexa))
print(hexa)
print(len(hexa))
