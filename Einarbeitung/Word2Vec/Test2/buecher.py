from xml.sax import make_parser, handler
import uuid
import codecs
import datetime
folder="../../../Korpora/Wikipedia/"
pagelocation = folder + "enwik9/pages1/"

class BuecherHandler(handler.ContentHandler):

    def __init__(self):
        self.current_content = ""

    def startElement(self, name, attrs):
        self.current_content = ""

    def characters(self, content):
        self.current_content += content

    def endElement(self, name):
        if name == "page" and not self.current_content.startswith('#redirect') and not self.current_content.startswith('#REDIRECT') and not self.current_content.startswith('#Redirect'):
            f = codecs.open(pagelocation+'page_'+str(uuid.uuid1()),"w","utf-8",errors='ignore')
            #f = open(pagelocation+'text'+str(uuid.uuid1()),'w')
            f.write('<text xml:space="preserve">')
            f.write(self.current_content)
            f.write('</text>')
            f.close()



print datetime.datetime.now()
parser = make_parser()
b = BuecherHandler()
parser.setContentHandler(b)
parser.parse(folder+"/enwik9/enwik9")
print 'done'
print datetime.datetime.now()
