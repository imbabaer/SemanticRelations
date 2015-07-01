import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def getSimilar(model,word,topn):
    retModel = model.most_similar(positive=[word], topn=topn)
    ret = ''
    for x in range(0,topn):
        ret += str(retModel[x][0])+' : '+str(retModel[x][1])+', '
    return ret

def testFunction(model,simfile,topn):
    testdatafile = open('testdata.txt','r')
    testdata = testdatafile.readlines()
    testdatafile.close()
    low = [10.0,'','']
    high = [0,'','']
    total=0
    found =0
    notfound = 0
    for td in testdata:
        total +=1
        td=td.replace('\n','')
        try:
            print model.most_similar(positive=[td], topn=topn)
            #num=4 if len(td)<4 else (20-len(td))/4
            #num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            ret = helpFunction1(model,simfile,topn,td,low,high)
            low = ret[0]
            high = ret[1]
            simfile.write('\n')
            found +=1

        except Exception, e:
            #num=4 if len(td)<4 else (20-len(td))/4
            #num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            simfile.write('-------------------------------\n')
            simfile.write('-, -, -, -, -\n')
            simfile.write('-------------------------------\n\n')
            print repr(e)
            notfound+=1

    printStatistics(simfile,low,high,total,found,notfound)
    simfile.close()

def printStatistics(simfile,low, high, total,found, notfound):
    simfile.write('Statistics:\n')
    simfile.write('Total testdata: '+str(total)+'\n')
    simfile.write('Found testdata: '+str(found)+'\n')
    simfile.write('NotFound testdata: '+str(notfound)+'\n')

    simfile.write('High:\n'+ 'search for: '+str(high[2])+'\t>\t'+str(high[1])+' : '+str(high[0])+'\n')
    simfile.write('Low:\n'+ 'search for: '+str(low[2])+'\t>\t'+ str(low[1])+' : '+str(low[0]))

def helpFunction1(model,simfile,topn,td,low,high):
    simfile.write('-------------------------------\n')
    ret = model.most_similar(positive=[td], topn=5)
    for x in range(0,topn):
        simfile.write(str(ret[x][0])+' : '+str(ret[x][1])+'\t\t||\t\t'+getSimilar(model,str(ret[x][0]),topn)+'\n')
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
            #print model.most_similar(positive=[td], topn=topn)
            #num=4 if len(td)<4 else (20-len(td))/4
            #num=num+1 if len(td)%4 != 0 else num
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
            #num=4 if len(td)<4 else (20-len(td))/4
            #num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            simfile.write('-------------------------------\n')
            simfile.write('-, -, -, -, -\n')
            simfile.write('-------------------------------\n\n')
            print repr(e)
            notfound+=1

    printStatistics(simfile,low,high,total,found,notfound)
    simfile.close()


def testFunction3(model,model2, model3, simfile,topn):
    testdatafile = open('testdata.txt','r')
    testdata = testdatafile.readlines()
    testdatafile.close()
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
            #print model.most_similar(positive=[td], topn=topn)
            #num=4 if len(td)<4 else (20-len(td))/4
            #num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            ret = helpFunction1(model,simfile,topn,td,low,high)
            low = ret[0]
            high = ret[1]
            ret = helpFunction1(model2,simfile,topn,td,low,high)
            low = ret[0]
            high = ret[1]
            ret = helpFunction1(model3,simfile,topn,td,low,high)
            low = ret[0]
            high = ret[1]
            simfile.write('\n')
            found +=1

        except Exception, e:
            #num=4 if len(td)<4 else (20-len(td))/4
            #num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            simfile.write('-------------------------------\n')
            simfile.write('-, -, -, -, -\n')
            simfile.write('-------------------------------\n\n')
            print repr(e)
            notfound+=1

    printStatistics(simfile,low,high,total,found,notfound)
    simfile.close()


#model = gensim.models.Word2Vec.load("../Test1/largeModel300105")
#model2 = gensim.models.Word2Vec.load("../Test1/techModel300105fullKorpustrained")
#model2 = gensim.models.Word2Vec.load("../Test1/largetrainedModel400825")

model3 = gensim.models.Word2Vec.load("../Test1/techModel300105")
print 'loaded model3'
simfile3 = open('recursiveTechSimilarities.txt','w')
#testFunction(model3,simfile3,5)

#model = gensim.models.Word2Vec.load("../Test1/largeModel300105")
print 'loaded model'
simfile4 = open('recursiveCombSimilarities_new.txt','w')
#testFunction2(model,model3,simfile4,5)



model4 = gensim.models.Word2Vec.load("../Test1/techModel300105fullKorpustrained")
print 'loaded model'
simfile4 = open('recursiveSimilarities_WithTechFullKorpusTrained.txt','w')
testFunction2(model4,model3,simfile4,5)
from Test1.soundtest import playTADA
playTADA()