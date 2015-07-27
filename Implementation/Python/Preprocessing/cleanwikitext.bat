REM Reinigung des kompletten Wikikorpus
perl ../../Implementation/Python/Preprocessing/wikicleaner.pl enwiki-latest-pages-articles.xml > enwiki-latest-pages-articles_clean.txt
REM Reinigung des kleinen Wikikorpus (1 Mrd Zeichen)
perl ../../Implementation/Python/Preprocessing/wikicleaner.pl enwik9 > enwik9_clean.txt