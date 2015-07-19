import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def getSimilar(model,word,topn):
    retModel = model.most_similar(positive=[word], topn=topn)
    ret = ''
    for x in range(0,topn):
        ret += str(retModel[x][0])+' : '+str(retModel[x][1])+', '
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

#write the data into the simfile
def helpFunction1(model,simfile,topn,td,low,high):
    simfile.write('-------------------------------\n')
    ret = model.most_similar(positive=[td], topn=5)
    for x in range(0,topn):
        str1=str(ret[x][0])+' : '+str(ret[x][1])
        simfile.write(str1+getTabs(str1,40)+'||\t'+getSimilar(model,str(ret[x][0]),topn)+'\n')
        if ret[x][1] < low[0]:
            low=[ret[x][1],ret[x][0],td]
        if ret[x][1] > high[0]:
            high=[ret[x][1],ret[x][0],td]
    simfile.write('-------------------------------\n')
    return [low,high]

def testFunction2(model,model2,simfile,topn):
    testdatafile = open('testdata.txt','r')
    testdata = testdatafile.readlines()
    testdatafile.close()
    #statistics for lowest and highest cosine similarity
    low = [10.0,'','']
    high = [0,'','']
    total=0
    found =0
    notfound = 0

    for td in testdata:
        total +=1
        td=td.replace('\n','')
        try:
            print td
            simfile.write(td+'\n')
            ret = helpFunction1(model,simfile,topn,td,low,high)
            low = ret[0]
            high = ret[1]
            ret = helpFunction1(model2,simfile,topn,td,low,high)
            low = ret[0]
            high = ret[1]
            simfile.write('\n')
            found +=1

        except Exception, e:
            simfile.write(td+'\n')
            simfile.write('-------------------------------\n')
            simfile.write('-, -, -, -, -\n')
            simfile.write('-------------------------------\n\n')
            print repr(e)
            notfound+=1

    printStatistics(simfile,low,high,total,found,notfound)
    simfile.close()



modelTech = gensim.models.Word2Vec.load("../Models/techModel300105")
print 'loaded modelTech'

modelFull = gensim.models.Word2Vec.load("../Models/largeModel300105")
print 'loaded modelFull'

simfile = open('recursiveCombinedSimilarities.txt','w')
testFunction2(modelFull,modelTech,simfile,5)
print 'done.'
