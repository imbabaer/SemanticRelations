import gensim
import nltk
import string
import time
import datetime
import numpy as np
from Test1.soundtest import playTADA

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
print datetime.datetime.now()
f = open ('t7times','w')
f.write(str((datetime.datetime.now())))
#fileenwik9preprocessed = open(folder+'enwik9/text')
#data = fileenwik9preprocessed.read()

file = open(folder+'lates-pages-articles_no-punctuation-and-lower_new','w')
#file = open(folder+'/enwik9/text__no-punctuation-and-lower','w')
#file = open(folder+'/enwik9/science_no-punctuation-and-lower','w')
#file = open(folder+'/enwik9/science_no-punctuation-and-lower','w')
#file = open(folder+'/pages/science_no-punctuation-and-lower','w')

x=0
#with open(folder+'enwiki-latest-pages-articles_clean_new.txt') as infile:
#with open(folder+'/enwik9/text') as infile:
with open(folder+'enwiki-latest-pages-articles_clean_new.txt') as infile:
    for line in infile:
        '''
        try:
            line=line.decode("utf8")
        except Exception, e:
            print repr(e)
        '''
        sents.extend(sent_tokenizer.tokenize(line))
        for sent in sents:
            sent = sent.replace("\n",".")
            for c in string.punctuation:
                sent=sent.replace(c,"")
            file.write(sent.lower())
            file.write('\n')
        print 'extend tokenized line: '+str(x)
        x+=1
        sents = []
print time.time()-starttime
print datetime.datetime.now()
f.write(str((datetime.datetime.now())))
f.close()
file.close()

playTADA()