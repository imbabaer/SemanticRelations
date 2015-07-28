'''
In diesem Skript werden Synonyme der Testdaten gesucht und analysiert.

dict.csv muss zuvor mittels dem SynonymListBuilder.py Skript erstellt werden.
'''
import gensim, logging
import csv
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def getSimilar(model,word,topn):
    retModel = model.most_similar(positive=[word], topn=topn)
    ret = []
    for x in range(0,topn):
        ret.append(retModel[x][0])
    return ret

def findSynonyms(model,simfile,topn,td,low,high,testdatadict):
    simfile.write('-------------------------------\n')
    ret = model.most_similar(positive=[td], topn=topn)
    synonymfound = False
    recursivewords = []
    synonym = ""
    for x in range(0,topn):
        #Rekursivaufruf der getSimilar-Methode
        rets= getSimilar(model,str(ret[x][0]),topn)
        for e in rets:
            recursivewords.append(e)
        #Fuer Statisik der Kosinusaehnlichkeiten
        if ret[x][1] < low[0]:
            low=[ret[x][1],ret[x][0],td]
        if ret[x][1] > high[0]:
            high=[ret[x][1],ret[x][0],td]

    #Suche in den 'recursivewords' solange, bis ein Eintrag in der Synonymliste vorhanden ist
    for entry in recursivewords:
        if (not synonymfound):
            synonymfound = entry in testdatadict[td]
            if(synonymfound):
                synonym = entry
                simfile.write(synonym+'\n')
                break
    syn = (synonymfound, synonym)
    simfile.write('-------------------------------\n')
    return [low,high,syn,not synonymfound]

def makeSimFile(model,testdatadict,simfile,topn):

    low = [10.0,'','']
    high = [0,'','']
    total=0
    found =0
    notfound = 0
    synonyms = []
    nosynonyms = []
    for td in sorted(testdatadict):
        total +=1
        td=td.replace('\n','')
        try:
            print td
            simfile.write(td+'\n')
            ret = findSynonyms(model,simfile,topn,td,low,high,testdatadict)
            low = ret[0]
            high = ret[1]
            syn = ret[2]
            nosyn = ret[3]
            if (syn[0]):
                synonyms.append((td,syn))
            if (nosyn):
                nosynonyms.append(td)

            simfile.write('\n')
            found +=1

        except Exception, e:
            simfile.write('-, -, -, -, -\n')
            simfile.write('-------------------------------\n\n')
            print type(e)
            print repr(e)
            notfound+=1

    simfile.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    simfile.write("Synonyms:\n")
    simfile.write("Synonyms found: "+ str(len(synonyms))+"\n")
    #Ausgabe der gefundenen Synonyme
    for syn in synonyms:
        simfile.write(syn[0]+"\t"+syn[1][1]+"\n")

    simfile.write("\nNo synonyms found: "+ str(len(nosynonyms))+"\n")
    simfile.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
    simfile.close()


mydict = {}
reader = csv.reader(open('../GetSynonyms/dict.csv', 'rb'))
mydict = dict(x for x in reader)
#Erstellen des bereinigten dictionary, in dem die Testdaten als key und die dazugehoerigen Synonyme in einer Liste als value stehen.
testdatadict={}
for key in sorted(mydict):
    value = mydict[key]
    #Wenn es Synoyme fuer diesen Testbegriff gibt
    if(value):
        values = value.split(",")
        cleaned_list = []
        for val in values:
            val = val.replace(";","")
            #durch das Entfernen von '-' (bei der Erstellung des dict.csv) kann es vorkommen, dass Synonyme gleich dem Testwort in der Liste stehen
            if(val != key):
                cleaned_list.append(val)
        if (len(cleaned_list)>0):
            testdatadict[key] = cleaned_list


model3 = gensim.models.Word2Vec.load("../Models/techModel300105")
print 'loaded model3'
simfileTech = open('SynonymsInTechModel.txt','w')

makeSimFile(model3,testdatadict,simfileTech,5)

model = gensim.models.Word2Vec.load("../Models/largeModel300105")
print 'loaded model'
simfileLargeModel = open('SynonymsInFullModel.txt','w')

makeSimFile(model,testdatadict,simfileLargeModel,5)


