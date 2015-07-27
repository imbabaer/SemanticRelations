from sklearn import svm
import os
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

def train(list, tags,path,files, tag):
    for file in files:
        f = open(path+'/'+file,'r')
        text = f.read()
        f.close()
        list.append(unicode(text))
        tags.append(tag)
    return list, tags

def testfunction(path,classifier):
    f = open(path,'r')
    #get the category and the probability of the fulltext
    ret = classifier.predict(f.read())
    f.close()
    #count the tech and nonTech categorized documents
    if ret[0]==1:
        #counttech +=1
        os.rename(path,os.path.dirname(path)+'/'+'tech'+os.path.basename(path))
    elif ret[0]==5:
        #countscience +=1
        os.rename(path,os.path.dirname(path)+'/'+'science'+os.path.basename(path))
    elif ret[0]==4:
        #countsport +=1
        os.rename(path,os.path.dirname(path)+'/'+'sport'+os.path.basename(path))
    elif ret[0]==2:
        #countentertainment +=1
        os.rename(path,os.path.dirname(path)+'/'+'entertainment'+os.path.basename(path))
    elif ret[0]==3:
        #countpolitic +=1
        os.rename(path,os.path.dirname(path)+'/'+'politic'+os.path.basename(path))
    elif ret[0] == '':
        os.rename(path,os.path.dirname(path)+'/'+'other'+os.path.basename(path))
    #print ret
    print os.path.basename(path)
    #countnews['test']+=1

categories = [(1,'tech'), (2,'entertainment'),(3,'politic'), (4,'sport'), (5,'science')]

countnews={}
countnews[1]=0
countnews[2]=0
countnews[3]=0
countnews[4]=0
countnews[5]=0

countnews['test']=0

countentertainment=0
counttech=0
countscience=0
countsport=0
countpolitic=0


countnontech=0
counttech=0

mypathtech='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/tech'
mypathentert='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/enternainment'
mypathpolitic='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/politic'
mypathscience='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/science'
mypathsport='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/sport'
#mypathtest='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/test'
#mypathtest='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/pages'
mypathtest ='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages/3/texts'
mypathtest2 ='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages'
classifierfilename = 'svmclassifier100.0001.pkl'

'''
import os.path
if os.path.isfile(classifierfilename):
    classifier = joblib.load(classifierfilename)
else:
    techfiles = get_filelist(mypathtech)
    entfiles = get_filelist(mypathentert)
    politicfiles = get_filelist(mypathpolitic)
    sciencefiles = get_filelist(mypathscience)
    sportfiles = get_filelist(mypathsport)
    print 'train model'
    print '\ttrain tech'
    train(mypathtech,techfiles,'tech',classifier)
    print '\ttrain entertainment'
    train(mypathentert,entfiles,'entertainment',classifier)
    print '\ttrain politic'
    train(mypathpolitic,politicfiles,'politic',classifier)
    print '\ttrain sport'
    train(mypathsport,sportfiles,'sport',classifier)
    print '\ttrain science'
    train(mypathscience,sciencefiles,'science',classifier)

'''
#testfiles = get_filelist(mypathtest)
techfiles = get_filelist(mypathtech)
entfiles = get_filelist(mypathentert)
politicfiles = get_filelist(mypathpolitic)
sciencefiles = get_filelist(mypathscience)
sportfiles = get_filelist(mypathsport)

categories = [(1,'tech'), (2,'entertainment'),(3,'politic'), (4,'sport'), (5,'science')]

import os.path
from sklearn.externals import joblib

if os.path.isfile(classifierfilename):
    classifier = joblib.load(classifierfilename)
else:
    classifier = Pipeline([('vect', CountVectorizer()),
                         ('tfidf', TfidfTransformer()),
                         ('clf', SGDClassifier(loss='hinge', penalty='l2',
                                               alpha=1e-4, n_iter=100, random_state=42)),
    ])
    list = []
    tags = []
    print 'train model'
    print '\ttrain entertainment'
    list, tags = train(list, tags,mypathentert,entfiles,2)
    print '\ttrain politic'
    list, tags = train(list, tags,mypathpolitic,politicfiles,3)
    print '\ttrain sport'
    list, tags = train(list, tags,mypathsport,sportfiles,4)
    print '\ttrain science'
    list, tags = train(list, tags,mypathscience,sciencefiles,5)
    print '\ttrain tech'
    list, tags = train(list, tags,mypathtech,techfiles,1)

    _ = classifier.fit(list, tags)


joblib.dump(classifier, classifierfilename)


print "--------------------News from test------------------------"

testfiles2=[]
print 'get testfiles'
for x in range(0,420):
    print str(x)
    list = get_filelist(mypathtest2+'/'+str(x)+'/texts')
    for fi in list:
        testfunction(mypathtest2+'/'+str(x)+'/texts/'+fi,classifier)

print 'done'
from Test1.soundtest import playTADA
playTADA()