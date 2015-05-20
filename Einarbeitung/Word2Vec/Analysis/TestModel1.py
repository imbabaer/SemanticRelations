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
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\t'*num+':\t')
            ret = model.most_similar(positive=[td], topn=5)
            a =[str(i[0]) for i in ret]
            simfile.write(str(a).replace('[','').replace(']','').replace('\'',''))
            simfile.write('\n')
        except Exception, e:
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\t'*num+':\t')
            simfile.write('\n')
            print repr(e)

    simfile.close()

def testFunction(model, model2,simfile):
    testdatafile = open('testdata.txt','r')
    testdata = testdatafile.readlines()
    testdatafile.close()
    for td in testdata:
        td=td.replace('\n','')
        try:
            print model.most_similar(positive=[td], topn=5)
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            ret = model.most_similar(positive=[td], topn=5)
            a =[str(i[0]) for i in ret]
            simfile.write(str(a).replace('[','').replace(']','').replace('\'','')+'\n')


        except Exception, e:
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            simfile.write('-, -, -, -, -\n')
            print repr(e)

        try:
            ret2 = model2.most_similar(positive=[td], topn=5)
            b =[str(i[0]) for i in ret2]
            simfile.write(str(b).replace('[','').replace(']','').replace('\'',''))
            simfile.write('\n\n')

        except Exception, e:
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write('-, -, -, -, -\n\n')
            print repr(e)


    simfile.close()


def testFunction(model, model2, model3,simfile):
    testdatafile = open('testdata.txt','r')
    testdata = testdatafile.readlines()
    testdatafile.close()
    for td in testdata:
        td=td.replace('\n','')
        try:
            print model.most_similar(positive=[td], topn=5)
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            ret = model.most_similar(positive=[td], topn=5)
            a =[str(i[0]) for i in ret]
            simfile.write(str(a).replace('[','').replace(']','').replace('\'','')+'\n')


        except Exception, e:
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write(td+'\n')
            simfile.write('-, -, -, -, -\n')
            print repr(e)

        try:
            ret2 = model2.most_similar(positive=[td], topn=5)
            b =[str(i[0]) for i in ret2]
            simfile.write(str(b).replace('[','').replace(']','').replace('\'',''))
            simfile.write('\n')

        except Exception, e:
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write('-, -, -, -, -\n')
            print repr(e)
        try:
            ret3 = model3.most_similar(positive=[td], topn=5)
            c =[str(i[0]) for i in ret3]
            simfile.write(str(c).replace('[','').replace(']','').replace('\'',''))
            simfile.write('\n\n')

        except Exception, e:
            num=4 if len(td)<4 else (20-len(td))/4
            num=num+1 if len(td)%4 != 0 else num
            simfile.write('-, -, -, -, -\n\n')
            print repr(e)

    simfile.close()


model = gensim.models.Word2Vec.load("../Test1/largeModel300105")
print 'loaded model'
simfile = open('similarities.txt','w')
#testFunction(model,simfile)

'''
model2.init_sims()
model2.save('../Test1/techModel300105')
'''

model2 = gensim.models.Word2Vec.load("../Test1/techModel300105fullKorpustrained")
print 'loaded model2'
simfile2 = open('similarities2.txt','w')
#testFunction(model2,simfile2)


model3 = gensim.models.Word2Vec.load("../Test1/techModel300105")
print 'loaded model3'
simfile3 = open('similarities3.txt','w')


#testFunction(model3,simfile3)



simfile4 = open('combinedsimilarities.txt','w')
#testFunction(model,model2,simfile4)


simfile5 = open('combinedsimilarities3.txt','w')
testFunction(model,model2, model3,simfile5)

from Test1.soundtest import playTADA
playTADA()