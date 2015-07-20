import gensim, logging
import csv
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def getSimilar(model,word,topn):
    retModel = model.most_similar(positive=[word], topn=topn)
    ret = []
    for x in range(0,topn):
        ret.append(retModel[x][0])
    return ret

def getTabs(string,length):
    x=int((length-len(string))/4)
    if int((length-len(string)))%4 != 0:
        x+=1
    if x > 0:
        x+=1
    else:
        x=1
    return '\t'*(x)


def printStatistics(simfile,low, high, total,found, notfound):
    simfile.write('Statistics:\n')
    simfile.write('Total testdata: '+str(total)+'\n')
    simfile.write('Found testdata: '+str(found)+'\n')
    simfile.write('NotFound testdata: '+str(notfound)+'\n')

    simfile.write('High:\n'+ 'search for: '+str(high[2])+'\t>\t'+str(high[1])+' : '+str(high[0])+'\n')
    simfile.write('Low:\n'+ 'search for: '+str(low[2])+'\t>\t'+ str(low[1])+' : '+str(low[0]))

def helpFunction1(model,simfile,topn,td,low,high,testdatadict):
    simfile.write('-------------------------------\n')
    ret = model.most_similar(positive=[td], topn=5)
    synonymfound = False
    recursivewords = []
    synonym = ""
    for x in range(0,topn):
        rets= getSimilar(model,str(ret[x][0]),topn)
        for e in rets:
            recursivewords.append(e)
        if ret[x][1] < low[0]:
            low=[ret[x][1],ret[x][0],td]
        if ret[x][1] > high[0]:
            high=[ret[x][1],ret[x][0],td]
    for entry in recursivewords:
        if (not synonymfound):
            synonymfound = entry in testdatadict[td]
            if(synonymfound):
                synonym = entry
                break
    syn = (synonymfound, synonym)
    simfile.write('-------------------------------\n')
    return [low,high,syn,not synonymfound]

def testFunction2(model,testdatadict,simfile,topn):

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
            ret = helpFunction1(model,simfile,topn,td,low,high,testdatadict)
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
            #num=4 if len(td)<4 else (20-len(td))/4
            #num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            simfile.write('-------------------------------\n')
            simfile.write('-, -, -, -, -\n')
            simfile.write('-------------------------------\n\n')
            print type(e)
            print repr(e)
            notfound+=1

    simfile.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n")
    simfile.write("Synonyms:\n")
    simfile.write("Synonyms found: "+ str(len(synonyms))+"\n")
    for syn in synonyms:
        simfile.write(syn[0]+"\t"+syn[1][1]+"\n")

    simfile.write("\nNo synonyms found: "+ str(len(nosynonyms))+"\n")
    simfile.write("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
    #printStatistics(simfile,low,high,total,found,notfound)
    simfile.close()



mydict = {}
reader = csv.reader(open('../GetSynonyms/dictBigHugeThesaurus.csv', 'rb'))
mydict = dict(x for x in reader)
testdatadict={}
for key in sorted(mydict):
    value = mydict[key]
    if(value):
        values = value.split(",")
        cleaned_list = []
        for val in values:
            if(val != key):
                cleaned_list.append(val)

        testdatadict[key] = cleaned_list


model3 = gensim.models.Word2Vec.load("../Test1/techModel300105")
print 'loaded model3'
simfile5 = open('SynonymsBigHugeThesaurusInTechModel.txt','w')

testFunction2(model3,testdatadict,simfile5,5)

model = gensim.models.Word2Vec.load("../Test1/largeModel300105")
print 'loaded model'
simfileLargeModel = open('SynonymsBigHugeThesaurusInFullModel.txt','w')

testFunction2(model,testdatadict,simfileLargeModel,5)



from Test1.soundtest import playTADA
playTADA()