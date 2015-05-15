import nltk
import string
import time
import numpy
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import datetime
file1 = open('science300105.txt','w')
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
model = gensim.models.Word2Vec(gensim.models.word2vec.LineSentence(folder+'pages/science_no-punctuation-and-lower'),size=300, window=10, min_count=5, workers=12)

file1.write("\nTrainingtime: "+str(time.time()-start_time))


model.save("scienceModel300105")



file1.write("\nTrainingtime: "+str(time.time()-start_time))

print 'over all time:'+str(time.time()-time1)
file1.write('\nover all time:'+str(time.time()-time1))
file1.write(str(datetime.datetime.now()))

print datetime.datetime.now()

file1.close()

print("done.")

from Test1.soundtest import playTADA
playTADA()