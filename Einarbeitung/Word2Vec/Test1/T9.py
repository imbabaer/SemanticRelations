import time
import string
import gensim

folder="../../../Korpora/Wikipedia/"
buildvoctime = time.time()
z=0
splittedSentences1 = []
with open(folder+'enwik9/largefilepart1') as infile:
    for line in infile:
        line = line.replace("\n",".")
        for c in string.punctuation:
            line=line.replace(c,"")
        splittedSentences1.append([x for x in line.lower().split(" ") if x])
        print "added splitted1 sentence: "+str(z)
        z+=1

z=0
splittedSentences2 = []
with open(folder+'enwik9/largefilepart2') as infile:
    for line in infile:
        line = line.replace("\n",".")
        for c in string.punctuation:
            line=line.replace(c,"")
        splittedSentences2.append([x for x in line.lower().split(" ") if x])
        print "added splitted2 sentence: "+str(z)
        z+=1
#sind irgendwie glaub alle zeichen durchgelaufen> 634522335
print time.time() - buildvoctime
model = gensim.models.Word2Vec(size=100, window=5, min_count=20, workers=8)
model.build_vocab(splittedSentences1)
model.train(splittedSentences2)
model.save('model')


