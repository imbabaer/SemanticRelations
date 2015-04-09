# import modules & set up logging
import gensim, logging
import os
'''
class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
sentences = MySentences('../../../Thesis/Abstract/') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)
'''

#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

sentences = [['woman', 'queen'],
             ['man', 'king'],
             ['woman', 'queen'],
             ['man', 'king'],
             ['woman', 'queen'],
             ['man', 'king'],
             ['woman', 'queen'],
             ['man', 'king'],
             ['woman', 'queen'],
             ['man', 'kangoroo'], ]
sentences2 = [['', 'anarchism', 'originated', 'as', 'a', 'term', 'of', 'abuse', 'first', 'used', 'against', 'early', 'working', 'class', 'radicals', 'including', 'the', 'diggers', 'of', 'the', 'english', 'revolution', 'and', 'the', 'sans', 'culottes', 'of', 'the', 'french', 'revolution'],
['whilst', 'the', 'term', 'is', 'still', 'used', 'in', 'a', 'pejorative', 'way', 'to', 'describe', 'any', 'act', 'that', 'used', 'violent', 'means', 'to', 'destroy', 'the', 'organization', 'of', 'society', '', 'it', 'has', 'also', 'been', 'taken', 'up', 'as', 'a', 'positive', 'label', 'by', 'self', 'defined', 'anarchists'],
['the', 'word', 'anarchism', 'is', 'derived', 'from', 'the', 'greek', 'without', 'archons', 'ruler', 'chief', 'king', '']]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences2, min_count=1)

#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
#model.doesnt_match("breakfast cereal dinner lunch".split())
print model.similarity('anarchism', 'originated')

print("done.")