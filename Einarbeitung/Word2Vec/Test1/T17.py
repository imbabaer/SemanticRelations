import os

def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

mypathtest2 ='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages'
techfile = open('D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages/sciencefile.txt', 'a')


for x in range(0,421):
    print str(x)
    list = get_filelist(mypathtest2+'/'+str(x)+'/texts')
    for fi in list:
        if fi.startswith('tech'):
            print fi
            with open(mypathtest2+'/'+str(x)+'/texts/'+fi,'r') as infile:
                techfile.writelines(infile.readlines())

techfile.close()
from Test1.soundtest import playTADA
playTADA()