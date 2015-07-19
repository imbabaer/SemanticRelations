#import nltk
import string
import time
import numpy
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import datetime

def getWikiFolder():
    return "../../../Korpora/Wikipedia/"

class ModelBuilder:
    def __init__(self,size, window, mincount, finalize,korpus, modelname, timefile):
        self.size = size
        self.window = window
        self.mincount=mincount
        self.modelname = modelname
        self.timefile=timefile
        self.finalize = finalize
        self.korpus = korpus


    def build(self):
        file1 = open(self.timefile,'w')
        print datetime.datetime.now()
        file1.write(str(datetime.datetime.now()))
        time1 = time.time()
        buildvoctime = time.time()
        start_time = time.time()
        print "\ntraining model"
        model = gensim.models.Word2Vec(gensim.models.word2vec.LineSentence(getWikiFolder()+self.korpus),size=self.size, window=self.window, min_count=self.mincount, workers=12)
        file1.write("\nTrainingtime: "+str(time.time()-start_time))
        if self.finalize:
            model.init_sims(replace=True)


        model.save(self.modelname)
        file1.write("\nTrainingtime: "+str(time.time()-start_time))

        print 'over all time:'+str(time.time()-time1)
        file1.write('\nover all time:'+str(time.time()-time1))
        file1.write(str(datetime.datetime.now()))

        print datetime.datetime.now()

        file1.close()

        print("Model builded.")

        return model