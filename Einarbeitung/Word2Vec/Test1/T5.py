import time
start_time = time.time()

tmp = []
tmp.extend("first")
tmp.extend("w")
tmp.extend("s")
tmp.extend("d")
tmp.extend("f")
tmp.extend("a")
tmp.extend("k")

f = open('testfile','w')
for item in tmp:
    f.write(item)
f.close()

f = open('time','w')
f.write(str(time.time()-start_time))
f.close()
readingstart = time.time()
print time.time()-readingstart