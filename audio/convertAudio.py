import os, re
import subprocess

path = 'D:/Reposotories/Audio/tech.imki.speech-splitter/output/badinter_INA_extrait/'
outPath = 'D:/Reposotories/Audio/tech.imki.speech-splitter/output/badinter_INA_extrait_converted/'


def sorted_alphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

filelist=sorted_alphanumeric(os.listdir(path))

for filename in filelist[:]: 
    
    subprocess.call('ffmpeg -i ' + path + filename + ' -ac 1 -b:a 256k -ar 16000 ' + outPath + filename, shell=True)

