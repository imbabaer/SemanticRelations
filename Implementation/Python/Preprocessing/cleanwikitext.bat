REM Reinigung des kompletten Wikikorpus. Auszufuehren im Ordner wo enwiki-latest-pages-articles.xml gespeichert ist
perl ../../Implementation/Python/Preprocessing/wikicleaner.pl enwiki-latest-pages-articles.xml > enwiki-latest-pages-articles_clean.txt
REM Reinigung des kleinen Wikikorpus (1 Mrd Zeichen). Auszufuehren im Ordner wo enwik9 gespeichert ist
perl ../../Implementation/Python/Preprocessing/wikicleaner.pl enwik9 > enwik9_clean.txt