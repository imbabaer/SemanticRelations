'''
Dieses Skript verarbeitet die vom Wiki-Markup gereinigten Texte sodass sie als Input für die Klasse 'gensim.models.word2vec.LineSentence' dienen.
Dazu muessen die Daten von Satzzeichen befreit, lowercase und je Zeile ein Satz sein.
'''
import nltk
import string
import time
import datetime

time1 = time.time()

#get sentences
folder="../../../Korpora/Wikipedia/"

sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sents = []

starttime = time.time()
print str(starttime)
print datetime.datetime.now()
f = open ('t7times','w')
f.write(str((datetime.datetime.now())))

#fileenwik9preprocessed = open(folder+'enwik9/text')
#data = fileenwik9preprocessed.read()

file = open(folder+'lates-pages-articles_no-punctuation-and-lower','w')
#file = open(folder+'/enwik9/tech_no-punctuation-and-lower','w')
#file = open(folder+'/enwik9/enwik9_no-punctuation-and-lower','w')

textfile = folder+'enwiki-latest-pages-articles_clean.txt'
#textfile = folder+'pages/tech-pages_clean.txt'
#textfile = folder+'/enwik9/enwik9_clean.txt'

x=0
with open(textfile) as infile:
    for line in infile:
        sents.extend(sent_tokenizer.tokenize(line))
        for sent in sents:
            sent = sent.replace("\n",".")
            for c in string.punctuation:
                sent=sent.replace(c,"")
            file.write(sent.lower())
            file.write('\n')
        print 'extend line: '+str(x)
        x+=1
        sents = []

file.close()

print time.time()-starttime
print datetime.datetime.now()
f.write(str((datetime.datetime.now())))
f.close()
