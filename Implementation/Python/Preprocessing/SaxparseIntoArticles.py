'''
In diesem Skript wird das komplette Wiki-XML File mit einem SAX-Parser geparst und in einzelne Artikel geschrieben.
'''
from xml.sax import make_parser, handler
import os
import codecs
import datetime
folder="../../../Korpora/Wikipedia/"
pagelocation = folder + "pages/"

class Counter:
    def __init__(self):
        self.count = 0

    def getNumber(self):
        self.count += 1
        return self.count

class ArtikelHandler(handler.ContentHandler):

    def __init__(self):
        self.current_content = u''
        self.counter = Counter()

    def startElement(self, name, attrs):
        self.current_content = u''

    def characters(self, content):
        self.current_content += content

    def endElement(self, name):
        #Der Artikeltext steht in <text>...</text> tags
        if name == "text" and not self.current_content.startswith('#redirect') and not self.current_content.startswith('#REDIRECT') and not self.current_content.startswith('#Redirect'):
            number = self.counter.getNumber()
            print str(number)
            #zur Unterteilung werden Unterordner angelegt
            subfolder= str(number/20000)+'/'
            if not os.path.exists(pagelocation+subfolder):
                os.makedirs(pagelocation+subfolder)
            #Schreiben der einzelnen Artikel in eigene Dateien
            f = codecs.open(pagelocation+subfolder+'page_'+str(number),"w","utf-8",errors='ignore')
            #um mit dem Perlskript die Daten zu reinigen, müssen dise in <text>...</text> tags stehen
            f.write('<text xml:space="preserve">')
            f.write(self.current_content)
            f.write('</text>')
            f.close()
            print 'done writing page: '+str(number)

times = open('saxparsertime.txt','w')
times.write(str(datetime.datetime.now()))
print datetime.datetime.now()

parser = make_parser()
b = ArtikelHandler()
parser.setContentHandler(b)
#parsen des Wiki XML-Files
parser.parse(open(folder+"enwiki-latest-pages-articles.xml"))

print 'done'
print datetime.datetime.now()
times.write(str(datetime.datetime.now()))
times.close()