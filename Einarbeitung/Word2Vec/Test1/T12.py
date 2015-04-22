from xml.dom import minidom
folder="../../../Korpora/Wikipedia/"
pagelocation = folder + "/enwik9/pages/"

doc = minidom.parse(folder+"/enwik9/enwik9")
print 'done parsing file'

pages = doc.getElementsByTagName("page")
print 'got all pages'
x=0
for page in pages:
    content = page.getElementsByTagName("page")[0]
    f = open(pagelocation+'page'+str(x),'w')
    f.write(content)
    f.close()
    print 'done writin page'+str(x)
