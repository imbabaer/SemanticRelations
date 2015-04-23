import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import datetime

print datetime.datetime.now()

questionwordsfile = open('../../../Korpora/questions-words.txt')
qwords = questionwordsfile.readlines()

qwordspp =[]
for line in qwords:
    qwordspp.append(line.lower().split(" "))

print 'start loading model'
model = gensim.models.Word2Vec.load("largetrainedModel2")
print 'done loading model'

print model.most_similar(positive=[qwordspp[1][1],qwordspp[1][2]], negative=[qwordspp[1][0]], topn=1)
print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)

model.accuracy('../../../Korpora/questions-words.txt')