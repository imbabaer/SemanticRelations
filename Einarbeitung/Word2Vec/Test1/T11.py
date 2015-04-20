import gensim
model = gensim.models.Word2Vec.load("trainedModel")
print 'loaded model'
model2 = gensim.models.Word2Vec.load("largetrainedModel")
print 'loaded model2'


print model.similarity('anarchism','agassi')
print model.similarity('anarchism','girl')
print model.similarity('anarchism','violence')

print model.doesnt_match("breakfast cereal dinner lunch".split())
print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)

print model2.most_similar(positive=['anarchism'], topn=10)
print model2.most_similar(positive=['Anarchism'], topn=10)
print model2.most_similar(positive=['agassi'], topn=10)
