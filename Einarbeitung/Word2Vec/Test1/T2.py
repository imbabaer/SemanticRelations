import gensim, logging
import os
import math
folder="../../../Korpora/Wikipedia/enwik9/"
originalKorpus = folder+"enwik9";
preprocessedKorpus = folder+"text";
tmpOriginal = folder + "tmpOriginal/"
tmpPreprocessed = folder + "tmpPreprocessed/"

if not os.path.exists(folder+tmpOriginal):
    os.makedirs(folder+tmpOriginal)

if not os.path.exists(folder+tmpPreprocessed):
    os.makedirs(folder+tmpPreprocessed)


'''
#original Korpus
file = open(originalKorpus)
lines= file.readlines()
lenght=len(lines)
partitionSize = int(math.ceil(lenght/100))

for x in range(1, 100):
    f = open(tmpOriginal+'file'+str(x),'w')
    print "created: original/file"+str(x)
    for y in range (0,partitionSize):
        f.write(lines[x*y])
    f.close()
'''


#preprocessed Korpus
file = open(preprocessedKorpus)
lines= file.readlines()
lenght=len(lines)
partitionSize = int(math.ceil(lenght/100))
'''
'''

for x in range(1, 100):
    f = open(tmpPreprocessed+'file'+str(x),'w')
    print "created: preprocessed/file"+str(x)
    for y in range (0,partitionSize):
        f.write(lines[x*y])
    f.close()
partlines = lines[1-1000]


print "done."



