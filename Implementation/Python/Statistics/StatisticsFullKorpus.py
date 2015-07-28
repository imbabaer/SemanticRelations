'''
In diesem Skript werden die Saetze und Worte des Gesamtkorpus gezaehlt.
'''
import time

starttime = time.time()
folder="../../../Korpora/Wikipedia/"
wordcount = 0
sentcount = 0

print 'start counting'
with open(folder+'lates-pages-articles_no-punctuation-and-lower_new') as infile:
    #jede Zeile entspricht einem Satz
    for line in infile:
        words = len(line.split())
        wordcount+= words
        #nur Zeilen in denen auch Text steht werden als Satz gezaehlt
        if words >1:
            sentcount+=1
        if sentcount % 100000 == 0:
            print str(sentcount)
passedtime = time.time() - starttime
outfile = open('statisticsWikiKorpus.txt','w')
outfile.write('wordcount: ')
outfile.write(str(wordcount))
outfile.write('\nsentencecount: ')
outfile.write(str(sentcount))
outfile.write('\ncalculated in '+str(passedtime)+' seconds.')

outfile.close()

print("done.")