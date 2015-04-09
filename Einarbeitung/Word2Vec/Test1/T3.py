import gensim
import nltk
import string



#logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
#get sentences
folder="../../../Korpora/Wikipedia/enwik9/"
originalKorpus = folder+"enwik9";
preprocessedKorpus = folder+"text";
tmpOriginal = folder + "tmpOriginal/"
tmpPreprocessed = folder + "tmpPreprocessed/"

#os.system("T2.py")

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sents = []
for x in range(0, 1):
    #preprocessed Korpus
    #file = codecs.open(tmpPreprocessed+"file"+str(x),"r","utf-8",errors='ignore')
    file = open(tmpPreprocessed+"file"+str(x))
    data= file.read()
    sents.extend(sent_tokenizer.tokenize(data))


splittedSents = []
for sent in sents:
    for c in string.punctuation:
        sent=sent.replace(c,"")
    splittedSents.append(sent.lower().split(" "))

print splittedSents[0]
print splittedSents[1]
print splittedSents[2]
# train word2vec
model = gensim.models.Word2Vec(splittedSents, min_count=1, size=50)

#print model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
#model.doesnt_match("breakfast cereal dinner lunch".split())
#print model.similarity('woman', 'man')
print model.similarity('organization','anarchism')

'''
'''
print("done.")