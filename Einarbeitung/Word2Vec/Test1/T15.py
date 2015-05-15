import os

mypathtech='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/tech'
mypathentert='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/enternainment'
mypathpolitic='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/politic'
mypathscience='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/science'
mypathsport='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/sport'
#mypathtest='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/classification/test'
mypathtest='D:/SoftwareProjects/SemanticRelations/Korpora/Wikipedia/enwik9/pages'

def get_filelist(path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)
        break
    return files

def write_filelist(files, filename):
    f=open(filename+".txt",'w')
    for file in files:
        f.write(file)
        f.write('\n')
    f.close()

techfiles = get_filelist(mypathtech)
entfiles = get_filelist(mypathentert)
politicfiles = get_filelist(mypathpolitic)
sciencefiles = get_filelist(mypathscience)
sportfiles = get_filelist(mypathsport)
testfiles = get_filelist(mypathtest)

write_filelist(techfiles,'techtrainfiles')
write_filelist(entfiles,'entertaintrainfiles')
write_filelist(politicfiles,'politictrainfiles')
write_filelist(sciencefiles,'sciencetrainfiles')
write_filelist(sportfiles,'sporttrainfiles')
write_filelist(testfiles,'testtrainfiles')

