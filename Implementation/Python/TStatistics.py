import time

starttime = time.time()
folder="../../../Korpora/Wikipedia/"
#largefile = open(folder+'lates-pages-articles_no-punctuation-and-lower_new','r')
wordcount = 0
sentcount = 0

print 'start counting'
with open(folder+'lates-pages-articles_no-punctuation-and-lower_new') as infile:
    for line in infile:
        words = len(line.split())
        wordcount+= words
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