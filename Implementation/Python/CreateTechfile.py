'''
In diesem Skript werden alle 'tech'-Artikel in einem Textfile zusammengefasst.
'''
import os

def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

mypathpages ='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages'
techfile = open('D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages/tech-pages_clean.txt', 'a')


for x in range(0,421):
    print str(x)
    list = get_filelist(mypathpages+'/'+str(x)+'/texts')
    for fi in list:
        if fi.startswith('tech'):
            print fi
            with open(mypathpages+'/'+str(x)+'/texts/'+fi,'r') as infile:
                techfile.writelines(infile.readlines())

techfile.close()