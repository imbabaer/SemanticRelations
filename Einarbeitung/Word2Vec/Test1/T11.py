import gensim
#model = gensim.models.Word2Vec.load("trainedModel")
#print 'loaded model'
model2 = gensim.models.Word2Vec.load("largetrainedModel2")
print 'loaded model2'


#print model.similarity('anarchism','agassi')
#print model.similarity('anarchism','girl')
#print model.similarity('anarchism','violence')
#
#print model.doesnt_match("breakfast cereal dinner lunch".split())
#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)

print 'agassi'
print model2.most_similar(positive=['agassi'], topn=5)
print 'laptop'
print model2.most_similar(positive=['laptop'], topn=5)
print 'windows'
print model2.most_similar(positive=['windows'], topn=5)
print 'ram'
print model2.most_similar(positive=['ram'], topn=5)
print 'cache'
print model2.most_similar(positive=['cache'], topn=5)
print 'processor'
print model2.most_similar(positive=['processor'], topn=5)
print 'python'
print model2.most_similar(positive=['python'], topn=5)
print 'java'
print model2.most_similar(positive=['java'], topn=5)