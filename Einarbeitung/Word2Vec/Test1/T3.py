import gensim
import nltk
import string
import time



#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#get sentences
folder="../../../Korpora/Wikipedia/enwik9/"
originalKorpus = folder+"enwik9";
preprocessedKorpus = folder+"text";
tmpOriginal = folder + "tmpOriginal/"
tmpPreprocessed = folder + "tmpPreprocessed/"

#os.system("T2.py")

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sents = []
for x in range(0, 1000):
    #preprocessed Korpus
    #file = codecs.open(tmpPreprocessed+"file"+str(x),"r","utf-8",errors='ignore')
    file = open(tmpPreprocessed+"file"+str(x))
    data= file.read()
    sents.extend(sent_tokenizer.tokenize(data))
    print "added sentences from file: "+str(x)

start_time = time.time()
model = gensim.models.Word2Vec( size=100, window=5, min_count=5, workers=8)

x=0
for sent in sents:
    for c in string.punctuation:
        sent=sent.replace(c,"")
    model.train(sent.lower().split(" "))
    print "added splitted sentence: "+str(x)
    x+=1

#print splittedSents[0]
#print splittedSents[1]
#print splittedSents[2]

# train word2vec
model.init_sims()
model.save("smlTrainedModel")
#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
#model.doesnt_match("breakfast cereal dinner lunch".split())
#print model.similarity('woman', 'man')
print model.similarity('anarchism','agassi')
print model['anarchism']

file1 = open('smltime.txt','w')
file1.write("Trainingtime: ")
file1.write(str(time.time()-start_time))
file1.close()
'''
'''
print("done.")