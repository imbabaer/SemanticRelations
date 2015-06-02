import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#model = gensim.models.Word2Vec.load("largetrainedModel2")
#model = gensim.models.Word2Vec.load("smallModel300105")
print 'loaded model'
model2 = gensim.models.Word2Vec.load("largetrainedModel400825")
print 'loaded model2'


#largeaccuracy = model.accuracy('../../../Korpora/questions-words.txt')
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