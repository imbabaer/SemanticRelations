REM Auszufuehren im Ordner 'D:\SoftwareProjects\SemanticRelations\Korpora\Wikipedia\pages\[0-420]\', hier sind immer 20k Artikel gespeichert
mkdir texts
for /f %%f in ('dir /b D:\SoftwareProjects\SemanticRelations\Korpora\Wikipedia\pages\0') do perl ../../../../Implementation/Python/Preprocessing/wikicleaner.pl %%f > texts/text%%f.txt
REM for /f %%f in ('dir /b D:\SoftwareProjects\SemanticRelations\Korpora\Wikipedia\pages\1') do perl ../../../../Implementation/Python/Preprocessing/wikicleaner.pl %%f > texts/text%%f.txt
REM usw.