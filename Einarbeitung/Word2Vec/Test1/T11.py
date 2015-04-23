import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = gensim.models.Word2Vec.load("trainedModel2")
print 'loaded model'
model2 = gensim.models.Word2Vec.load("trainedModel3")
print 'loaded model2'


#print model.similarity('anarchism','agassi')
#print model.similarity('anarchism','girl')
#print model.similarity('anarchism','violence')
#
#print model.doesnt_match("breakfast cereal dinner lunch".split())
#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)

print 'agassi'
print model2.most_similar(positive=['agassi'], topn=5)
try:
    print model.most_similar(positive=['agassi'], topn=5)
except Exception, e:
    print repr(e)
print 'laptop'
print model2.most_similar(positive=['laptop'], topn=5)
try:
    print model.most_similar(positive=['laptop'], topn=5)
except Exception, e:
    print repr(e)
print 'windows'
print model2.most_similar(positive=['windows'], topn=5)
try:
    print model.most_similar(positive=['windows'], topn=5)
except Exception, e:
    print repr(e)
print 'ram'
print model2.most_similar(positive=['ram'], topn=5)
try:
    print model.most_similar(positive=['ram'], topn=5)
except Exception, e:
    print repr(e)
print 'cache'
print model2.most_similar(positive=['cache'], topn=5)
try:
    print model.most_similar(positive=['cache'], topn=5)
except Exception, e:
    print repr(e)
print 'processor'
print model2.most_similar(positive=['processor'], topn=5)
try:
    print model.most_similar(positive=['processor'], topn=5)
except Exception, e:
    print repr(e)
print 'python'
print model2.most_similar(positive=['python'], topn=5)
try:
    print model.most_similar(positive=['python'], topn=5)
except Exception, e:
    print repr(e)
print 'java'
print model2.most_similar(positive=['java'], topn=5)
try:
    print model.most_similar(positive=['java'], topn=5)
except Exception, e:
    print repr(e)

print model2.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
model.accuracy('../../../Korpora/questions-words.txt')
model2.accuracy('../../../Korpora/questions-words.txt')