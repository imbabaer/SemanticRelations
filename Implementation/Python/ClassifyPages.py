'''
In diesem Skript wird der NBC erstellt, trainiert und die einzelnen Wikipediaartikel klassifiziert.
'''
import docclass as doc
import os



def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

def train(path,files, tag,classifier):
    for file in files:
        f = open(path+'/'+file,'r')
        classifier.train(f.read(),tag)
        f.close()
        countnews[tag]+=1

def classify(path,classifier):
       f = open(path,'r')
       #get the category and the probability of the fulltext
       ret = classifier.getCat(f.read())
       f.close()
       if ret[0]=='tech':
           os.rename(path,os.path.dirname(path)+'/'+'tech'+os.path.basename(path))
       elif ret[0]=='science':
           os.rename(path,os.path.dirname(path)+'/'+'science'+os.path.basename(path))
       elif ret[0]=='sport':
           os.rename(path,os.path.dirname(path)+'/'+'sport'+os.path.basename(path))
       elif ret[0]=='entertainment':
           os.rename(path,os.path.dirname(path)+'/'+'entertainment'+os.path.basename(path))
       elif ret[0]=='politic':
           os.rename(path,os.path.dirname(path)+'/'+'politic'+os.path.basename(path))
       elif ret[0] == '':
           os.rename(path,os.path.dirname(path)+'/'+'other'+os.path.basename(path))
       print ret


countnews={}
countnews['tech']=0
countnews['science']=0
countnews['politic']=0
countnews['sport']=0
countnews['entertainment']=0



#create classifier with function 'getwords', minlength = 3, maxlength = 20
classifier = doc.Classifier(doc.getwords,3,20)


mypathtech='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/tech'
mypathentert='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/enternainment'
mypathpolitic='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/politic'
mypathscience='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/science'
mypathsport='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/sport'
mypathpages ='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/pages'


print 'train model'
print '\ttrain tech'
techfiles = get_filelist(mypathtech)
train(mypathtech,techfiles,'tech',classifier)
print '\ttrain entertainment'
entfiles = get_filelist(mypathentert)
train(mypathentert,entfiles,'entertainment',classifier)
print '\ttrain politic'
politicfiles = get_filelist(mypathpolitic)
train(mypathpolitic,politicfiles,'politic',classifier)
print '\ttrain sport'
sportfiles = get_filelist(mypathsport)
train(mypathsport,sportfiles,'sport',classifier)
print '\ttrain science'
sciencefiles = get_filelist(mypathscience)
train(mypathscience,sciencefiles,'science',classifier)



print 'classify pages'
for x in range(0,421):
    print str(x)
    list = get_filelist(mypathpages+'/'+str(x)+'/texts')
    for fi in list:
        classify(mypathpages+'/'+str(x)+'/texts/'+fi,classifier)
print 'done'