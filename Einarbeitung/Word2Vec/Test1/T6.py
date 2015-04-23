import nltk
import string
import time
import numpy
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
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

buildvoctime = time.time()

print "\ntraining model"
print
start_time = time.time()
# train word2vec
model = gensim.models.Word2Vec(gensim.models.word2vec.LineSentence(folder+'enwik9/text__no-punctuation-and-lower'),size=600, window=8, min_count=20, workers=12)

file1.write("\nTrainingtime: "+str(time.time()-start_time))


model.save("trainedModel3")



file1.write("\nTrainingtime: "+str(time.time()-start_time))

print 'over all time:'+str(time.time()-time1)
file1.write('\nover all time:'+str(time.time()-time1))
file1.write(str(datetime.datetime.now()))

print datetime.datetime.now()

file1.close()

print("done.")