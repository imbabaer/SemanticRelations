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
             ['man', 'king'], ]
# train word2vec on the two sentences
model = gensim.models.Word2Vec(sentences, min_count=1)

print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
#model.doesnt_match("breakfast cereal dinner lunch".split())
print model.similarity('woman', 'man')

print("done.")