import nltk
import string
import time
import numpy
import gensim
import datetime
file1 = open('times.txt','w')
print datetime.datetime.now()
file1.write(str(datetime.datetime.now()))

time1 = time.time()

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#get sentences
folder="../../../Korpora/Wikipedia/"
#tmpPreprocessed = folder + "latest-pages-tmpPreprocessed/"
tmpPreprocessed = folder + "enwik9/tmpPreprocessed/"
'''
sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sents = []
for x in range(0, 16):
    #preprocessed Korpus
    #file = codecs.open(tmpPreprocessed+"file"+str(x),"r","utf-8",errors='ignore')
    file = open(tmpPreprocessed+"file"+str(x))
    data= file.read()
    sents.extend(sent_tokenizer.tokenize(data))
    print "added sentences from file: "+str(x)
    '''
'''
readingstart = time.time()
now = datetime.datetime.now()
print "start reading file (" + now.strftime("%H:%M:%S")+")"
readingstart = time.time()
file = open(folder+"enwik9/text")
data= file.read()
sents.extend(sent_tokenizer.tokenize(data))
now = datetime.datetime.now()
print "done reading file (" + now.strftime("%H:%M:%S")+")"
print "time reading file: "+str(time.time()-readingstart)
'''
'''
start_time = time.time()
print "reading file"
file = open(folder+'lates-pages-articles')
data= file.read()
print time.time()-start_time
file1.write('reading file time: '+str(time.time()-start_time))
'''
buildvoctime = time.time()
z=0
'''
splittedSentences = []
with open(folder+'lates-pages-articles') as infile:
    for line in infile:
        line = line.replace("\n",".")
        for c in string.punctuation:
            line=line.replace(c,"")
        #model.build_vocab([x for x in line.lower().split(" ") if x])
        splittedSentences.append([x for x in line.lower().split(" ") if x])
        print "added splitted sentence: "+str(z)
        z+=1
print time.time() - buildvoctime

file1.write('\nbuild voc time: '+str(time.time()-buildvoctime))
'''
'''
print time.time()-time1

file1.write("Time: ")
file1.write(str(time.time()-time1))
file1.close()
'''

print "\ntraining model"
print
start_time = time.time()
# train word2vec
model = gensim.models.Word2Vec(gensim.models.word2vec.LineSentence(folder+'lates-pages-articles_no-punctuation-and-lower'),size=200, window=5, min_count=20, workers=12)

file1.write("\nTrainingtime: "+str(time.time()-start_time))

#model.init_sims()
model.save("largetrainedModel2")
#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
#model.doesnt_match("breakfast cereal dinner lunch".split())
#print model.similarity('woman', 'man')
#print model.similarity('anarchism','agassi')
#print model.similarity('anarchism','violence')


file1.write("\nTrainingtime: "+str(time.time()-start_time))

'''
'''
print 'over all time:'+str(time.time()-time1)
file1.write('\nover all time:'+str(time.time()-time1))
file1.write(str(datetime.datetime.now()))

print datetime.datetime.now()

file1.close()

print("done.")