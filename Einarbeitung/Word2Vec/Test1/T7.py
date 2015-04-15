import gensim
import nltk
import string
import time
import numpy as np

time1 = time.time()

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#get sentences
folder="../../../Korpora/Wikipedia/"
#tmpPreprocessed = folder + "latest-pages-tmpPreprocessed/"
tmpPreprocessed = folder + "enwik9/tmpPreprocessed/"

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sents = []
'''
for x in range(0, 84):
    #preprocessed Korpus
    #file = codecs.open(tmpPreprocessed+"file"+str(x),"r","utf-8",errors='ignore')
    file = open(tmpPreprocessed+"file"+str(x))
    data= file.read()
    sents.extend(sent_tokenizer.tokenize(data))
    print "added sentences from file: "+str(x)
   '''
starttime = time.time()
print str(starttime)
#fileenwik9preprocessed = open(folder+'enwik9/text')
#data = fileenwik9preprocessed.read()

x=0
with open(folder+'enwik9/text') as infile:
    for line in infile:
        sents.extend(sent_tokenizer.tokenize(line))
        print 'extend tokenized line: '+str(x)
        x+=1
print time.time()-starttime

file = open(folder+'enwik9/largefile2','w')
x=0
for sent in sents:
    file.write(sent)
    file.write('\n')
    print 'write sent: '+str(x)
    x+=1
file.close()

