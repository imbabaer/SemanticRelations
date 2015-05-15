from xml.sax import make_parser, handler
import os
import codecs
import datetime
from Test1.soundtest import playWAV
folder="../../../Korpora/Wikipedia/"
#pagelocation = folder + "enwik9/pagesTest2/"
pagelocation = folder + "pages/"

class Counter:
    def __init__(self):
        self.count = 0

    def getNumber(self):
        self.count += 1
        return self.count

class BuecherHandler(handler.ContentHandler):

    def __init__(self):
        self.current_content = u''
        self.counter = Counter()

    def startElement(self, name, attrs):
        self.current_content = u''

    def characters(self, content):
        self.current_content += content

    def endElement(self, name):
        if name == "text" and not self.current_content.startswith('#redirect') and not self.current_content.startswith('#REDIRECT') and not self.current_content.startswith('#Redirect'):
            number = self.counter.getNumber()
            print str(number)
            if number > 5742098:
                subfolder= str(number/20000)+'/'
                if not os.path.exists(pagelocation+subfolder):
                    os.makedirs(pagelocation+subfolder)
                f = codecs.open(pagelocation+subfolder+'page_'+str(number),"w","utf-8",errors='ignore')
                #f = open(pagelocation+'text'+str(uuid.uuid1()),'w')
                f.write('<text xml:space="preserve">')
                f.write(self.current_content)
                f.write('</text>')
                f.close()
                print 'done writing page: '+str(number)

times = open('saxparsertime.txt','w')
times.write(str(datetime.datetime.now()))
playWAV('tada.wav')
print datetime.datetime.now()
parser = make_parser()
b = BuecherHandler()
parser.setContentHandler(b)
parser.parse(open(folder+"enwiki-latest-pages-articles.xml"))
print 'done'
print datetime.datetime.now()
times.write(str(datetime.datetime.now()))
times.close()
playWAV('tada.wav')