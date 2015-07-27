import time

starttime = time.time()
folder="../../../Korpora/Wikipedia/"
#largefile = open(folder+'lates-pages-articles_no-punctuation-and-lower_new','r')
wordcount = 0
sentcount = 0

print 'start counting'
with open(folder+'pages/tech_no-punctuation-and-lower') as infile:
    for line in infile:
        wordcount+=len(line.split())
        sentcount+=1



import os
def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

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