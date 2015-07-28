'''
In diesem Skript werden die Accuracys der einzelnen Modelle ausgewertet.
'''
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

model = gensim.models.Word2Vec.load("../Models/largeModel300105")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')

model2 = gensim.models.Word2Vec.load("../models/techModel300105")
print 'loaded model2'
model2.accuracy('../../../Korpora/questions-words.txt')


'''
#Zum Test der Parameter-Testmodelle

model = gensim.models.Word2Vec.load("../Models/Testkorpora/small100105")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')

model = gensim.models.Word2Vec.load("../Models/Testkorpora/small1001010")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')


model = gensim.models.Word2Vec.load("../Models/Testkorpora/small200105")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')

model = gensim.models.Word2Vec.load("../Models/Testkorpora/small2001010")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')


model = gensim.models.Word2Vec.load("../Models/Testkorpora/small300105")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')

model = gensim.models.Word2Vec.load("../Models/Testkorpora/small3001010")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')


model = gensim.models.Word2Vec.load("../Models/Testkorpora/small400105")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')

model = gensim.models.Word2Vec.load("../Models/Testkorpora/small4001010")
print 'loaded model'
model.accuracy('../../../Korpora/questions-words.txt')
'''