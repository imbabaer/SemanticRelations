mkdir texts
for /f %%f in ('dir /b D:\SoftwareProjects\SemanticRelations\Korpora\Wikipedia\pages\0') do perl ../../../../Implementation/Python/Preprocessing/wikicleaner.pl %%f > texts/text%%f.txt