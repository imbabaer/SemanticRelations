import gensim, logging
import os
import math
folder="../../../Korpora/Wikipedia/"
preprocessedKorpus = folder+"enwiki-latest-pages-articles_clean.txt";
tmpPreprocessed = folder + "latest-pages-tmpPreprocessed/"

if not os.path.exists(tmpPreprocessed):
    os.makedirs(tmpPreprocessed)


#preprocessed Korpus
x = 0
y=0
tmp = []
with open(preprocessedKorpus) as infile:
    for line in infile:
        if x < 100000:
            tmp.extend(line)
            x+=1
        else:
            f = open(tmpPreprocessed+'file'+str(y),'w')
            for item in tmp:
                f.write(item)
            f.close()
            print "created: preprocessed/file"+str(y)
            tmp=[]
            x=0
            y+=1

'''
lines= file.read()
lenght=len(lines)
numFiles = 10000
partitionSize = int(math.ceil(lenght/numFiles))

for x in range(0, numFiles):
    f = open(tmpPreprocessed+'file'+str(x),'w')
    for y in range (0,partitionSize):
        f.write(lines[x*partitionSize +y])
    f.close()
    print "created: preprocessed/file"+str(x)
'''
print "done."



