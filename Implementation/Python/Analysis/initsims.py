'''
Finalisierung der Modelle, sofern nicht schon beim Erstellen erledigt.
'''
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

modelTech = gensim.models.Word2Vec.load("../Models/techModel300105")
print 'loaded modelTech'

modelFull = gensim.models.Word2Vec.load("../Models/largeModel300105")
print 'loaded modelFull'

modelTech.init_sims(replace=True)
print 'techmodel finalized'

modelFull.init_sims(replace=True)
print 'full model finalized'

