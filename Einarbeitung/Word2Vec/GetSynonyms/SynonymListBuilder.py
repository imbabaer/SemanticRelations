'''
parts from: https://github.com/Nucc/Thesaurus/blob/master/thesaurus.py
'''
import csv
from xml.dom.minidom import parse, parseString

import json

try:
    from urllib.request import urlopen
    from urllib.parse import urlparse
    from urllib.parse import quote
    from urllib.error import HTTPError
except ImportError:
    from urlparse import urlparse
    from urllib import quote
    from urllib2 import urlopen
    from urllib2 import HTTPError

class NoResultError(Exception):
  def __init__(self, message):
    self.message = message;

  def __str__(self):
    return repr(self.message)

class SynonymList:
    def __init__(self,testdatafile):
        self.testdatafile = testdatafile
        self.api_key="oa69e0MqIWBBjPH15AEJ"
        self.language="en_US"
        self.dict = {}
        self.noResults = 0



    def build(self):
        tfile = open(self.testdatafile,'r')
        testdata = tfile .readlines()
        tfile.close()

        for td in testdata:
            td = td.replace("\n","")
            self.processWord(td)
            self.dict[td]=self.results

    def show(self):
        for pair in self.dict:
            print pair
        print str(self.noResults)+" of "+str(len(self.dict)) +" words could not be found."

    def printToFile(self):
        writer = csv.writer(open('dict.csv', 'wb'))
        for key, value in self.dict.items():
           newVal = ','.join(value)
           writer.writerow([key, newVal])




    def get_json_from_api(self):
        word = quote(self.word)
        url = "http://thesaurus.altervista.org/thesaurus/v1?key=%s&word=%s&language=%s&output=json" % (self.api_key, word, self.language)
        response = urlopen(url)
        content = response.read().decode('utf-8')
        response.close()
        return json.loads(content)

    def processWord(self, word):
        self.word = word
        if self.word is None or len(self.word) == 0:
          self.view.set_status("Thesaurus", "Please select a word first!")
          return

        try:
          self.results = self.synonyms()
        except NoResultError:
            # nothing was found, look for alternatives
            print "no results for "+word
            self.results = []
            self.noResults +=1


    def synonyms(self):
        result = []
        try:
            data = self.get_json_from_api()
            for entry in data["response"]:
                result.append((entry["list"]["synonyms"].replace(" ","").replace("-","").replace("(antonym)","").replace("(similarterm)","").replace("(relatedterm)","").lower().split("|")))
        except (KeyError, HTTPError):
            if 'data' in locals():
                raise NoResultError(data["error"])
            else:
                raise NoResultError("Word not found.")

        r = list(set([item for sublist in result for item in sublist]))

        return r


sl = SynonymList("../Analysis/testdata.txt")
sl.build()
sl.show()

sl.printToFile()

print 'done.'