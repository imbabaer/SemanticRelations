
folder="../../../Korpora/Wikipedia/"
tmpPreprocessed = folder + "enwik9/tmpPreprocessed/"

file = open(folder+'enwik9/largefile2')
data= file.read()
outfile = open(folder+'enwik9/outfile.txt',"w")
x=0
with open(folder+'enwik9/largefile2') as infile:
    for line in infile:
        outfile.write(data[x])
        print 'written data['+str(x)+']'
        x+=1
outfile.close()