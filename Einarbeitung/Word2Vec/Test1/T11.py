import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#model = gensim.models.Word2Vec.load("largetrainedModel2")
model = gensim.models.Word2Vec.load("smallModel300105")
print 'loaded model'
model2 = gensim.models.Word2Vec.load("scienceModel300105")
print 'loaded model2'


#print model.similarity('anarchism','agassi')
#print model.similarity('anarchism','girl')
#print model.similarity('anarchism','violence')
#
#print model.doesnt_match("breakfast cereal dinner lunch".split())
#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
'''
print 'los angeles'
try:
    print model.most_similar(positive=['los_angeles'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['angeles'], topn=5)

print 'laptop'
try:
    print model.most_similar(positive=['laptop'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['laptop'], topn=5)

print 'windows'
try:
    print model.most_similar(positive=['windows'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['windows'], topn=5)

print 'ram'
try:
    print model.most_similar(positive=['ram'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['ram'], topn=5)

print 'cache'
try:
    print model.most_similar(positive=['cache'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['cache'], topn=5)

print 'processor'
try:
    print model.most_similar(positive=['processor'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['processor'], topn=5)

print 'python'
try:
    print model.most_similar(positive=['python'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['python'], topn=5)

print 'java'
try:
    print model.most_similar(positive=['java'], topn=5)
except Exception, e:
    print repr(e)
print model2.most_similar(positive=['java'], topn=5)

print model2.most_similar(positive=['euro', 'switzerland'], negative=['germany'], topn=1)
print model.most_similar(positive=['euro', 'switzerland'], negative=['germany'], topn=1)
print model2.most_similar(positive=['king', 'woman'], negative=['man'], topn=1)
print model2.most_similar(positive=['man', 'queen'], negative=['king'], topn=1)
'''
largeaccuracy = model.accuracy('../../../Korpora/questions-words.txt')
other = model2.accuracy('../../../Korpora/questions-words.txt')
'''
file = open("accuracylargetrainedModel300105.txt","w")
file.write('largefile')
file.write('\n')
'''
'''
for line in largeaccuracy:
    file.write(str(line))
    file.write('\n')
'''
'''
file.write('\n')
file.write('smallfile')
file.write('\n')

for line in other:
    file.write(str(line))
    file.write('\n')
file.close()
'''