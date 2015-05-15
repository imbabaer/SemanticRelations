import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



def testFunction(model,simfile):
    testdatafile = open('testdata.txt','r')
    testdata = testdatafile.readlines()
    testdatafile.close()
    for td in testdata:
        td=td.replace('\n','')
        try:
            print model.most_similar(positive=[td], topn=5)
            simfile.write(td+'\t:\t')
            simfile.write(str(model.most_similar(positive=[td], topn=5)))
            simfile.write('\n')
        except Exception, e:
            print repr(e)

    simfile.close()


'''
model = gensim.models.Word2Vec.load("../Test1/largetrainedModel300105")
print 'loaded model'
simfile = open('similarities.txt','w')
testFunction(model,simfile)
'''
'''
model2.init_sims()
model2.save('../Test1/techModel300105')
'''

model2 = gensim.models.Word2Vec.load("../Test1/techModel300105")
print 'loaded model2'
simfile2 = open('similarities2.txt','w')




testFunction(model2,simfile2)




