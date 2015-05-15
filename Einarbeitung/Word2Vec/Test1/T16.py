import os
from Test1.soundtest import playWAV
def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

mypath ='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/science/'
files = get_filelist(mypath)

f = open('D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/sciencetext.txt','w')

for file in files:
    lines = open(mypath+file,'r').readlines()
    for line in lines:
        f.write(line)
f.close()

playWAV('tada.wav')