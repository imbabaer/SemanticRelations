'''
In diesem Skript werden die Saetze und Worte des Technologiekorpus gezaehlt.
Ausserdem werden alle Artikel gezaehlt, die mit 'tech' klassifiziert wurden.
'''
import time
import os

def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files


starttime = time.time()
folder="../../../Korpora/Wikipedia/"
wordcount = 0
sentcount = 0

print 'start counting'
with open(folder+'pages/tech_no-punctuation-and-lower') as infile:
    for line in infile:
        words = len(line.split())
        wordcount+= words
        if words >1:
            sentcount+=1
        if sentcount % 100000 == 0:
            print str(sentcount)



mypathpages ='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages'


articles=0

for x in range(0,421):
    print str(x)
    list = get_filelist(mypathpages+'/'+str(x)+'/texts')
    for fi in list:
        if fi.startswith('tech'):
           articles+=1
        print str(articles)

passedtime = time.time() - starttime
outfile = open('statisticsTechWikiKorpus.txt','w')
outfile.write('wordcount: ')
outfile.write(str(wordcount))
outfile.write('\nsentencecount: ')
outfile.write(str(sentcount))
outfile.write('\narticlecount: ')
outfile.write(str(articles))
outfile.write('\ncalculated in '+str(passedtime)+' seconds.')

outfile.close()

print("done.")