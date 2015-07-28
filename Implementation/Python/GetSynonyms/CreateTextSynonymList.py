'''
In diesem Skript werden eine Liste mit allen Testdaten und den dazugehoerigen Synonymen erstellt und in eine Textdatei
geschrieben, sowie eine Liste mit allen Woertern, die auch Synonyme besitzen.
dict.csv muss zuvor mittels dem SynonymListBuilder.py Skript erstellt werden.
'''
import csv
mydict = {}
reader = csv.reader(open('dict.csv', 'rb'))
mydict = dict(x for x in reader)

f = open("FullSynonymliste.txt",'w')
for key in sorted(mydict):
    value = mydict[key]
    values = value.split(",")
    cleaned_list = []
    for val in values:
        if(val != key):
            cleaned_list.append(val)
    f.write(key+"\t"+",".join(cleaned_list))
    f.write("\n")

f.close()


f = open("Synonymliste.txt",'w')
for key in sorted(mydict):
    value = mydict[key]

    if(value):
        values = value.split(",")
        cleaned_list = []
        for val in values:
            if(val != key):
                cleaned_list.append(val)
        f.write(key+"\t"+",".join(cleaned_list))
        f.write("\n")
f.close()


print "done"