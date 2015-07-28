'''
In diesem Skript werden die aehnlichen Worte der Testbegriffe in ein Textfile geschrieben.
'''
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def printStatistics(simfile,low, high, total,found, notfound):
    simfile.write('Statistics:\n')
    simfile.write('Total testdata: '+str(total)+'\n')
    simfile.write('Found testdata: '+str(found)+'\n')
    simfile.write('NotFound testdata: '+str(notfound)+'\n')

    #Worte mit hoechster und niedrigster Kosinusaehnlichkeit werden ausgegeben
    simfile.write('High:\n'+ 'search for: '+str(high[2])+'\t>\t'+str(high[1])+' : '+str(high[0])+'\n')
    simfile.write('Low:\n'+ 'search for: '+str(low[2])+'\t>\t'+ str(low[1])+' : '+str(low[0]))

#write the data into the simfile
def writeSimilaritiesToFile(model,simfile,topn,td,low,high):
    simfile.write('-------------------------------\n')
    ret = model.most_similar(positive=[td], topn=topn)
    for x in range(0,topn):
        str1=str(ret[x][0])+' : '+str(ret[x][1])
        simfile.write(str1+'\n')
        #Auswertung fuer Kosinusaehnlichkeit-Statistik
        if ret[x][1] < low[0]:
            low=[ret[x][1],ret[x][0],td]
        if ret[x][1] > high[0]:
            high=[ret[x][1],ret[x][0],td]
    simfile.write('-------------------------------\n')
    return [low,high]

def makeSimFile(model,model2,simfile,topn):
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
            ret = writeSimilaritiesToFile(model,simfile,topn,td,low,high)
            low = ret[0]
            high = ret[1]
            ret = writeSimilaritiesToFile(model2,simfile,topn,td,low,high)
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

simfile = open('CombinedSimilarities.txt','w')
makeSimFile(modelFull,modelTech,simfile,5)
print 'done.'

