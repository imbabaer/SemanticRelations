
folder="../../../Korpora/Wikipedia/"
lf1 = open(folder+'enwik9/largefilepart1',"w")
lf2 = open(folder+'enwik9/largefilepart2',"w")
lf3 = open(folder+'enwik9/largefilepart3',"w")
x=0
with open(folder+'enwik9/largefile2') as infile:
    for line in infile:
        if x<7000000:
            lf1.write(line)
            print 'line ['+str(x)+']'
            x+=1
        elif x<14000000:
            lf2.write(line)
            print 'line ['+str(x)+']'
            x+=1
        else:
            lf3.write(line)
            print 'line ['+str(x)+']'
            x+=1

lf1.close()
lf2.close()
