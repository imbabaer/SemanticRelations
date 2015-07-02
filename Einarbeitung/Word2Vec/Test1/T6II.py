import T6
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

modelbuilder=T6.ModelBuilder(300, 10, 5, True ,'pages/tech_no-punctuation-and-lower', 'testkorpora/tech300105', 'testkorpora/tech300105times.txt')
model = modelbuilder.build()
#model.accuracy('../../../Korpora/questions-words.txt')

#enwik9/text__no-punctuation-and-lower
#pages/tech_no-punctuation-and-lower
#lates-pages-articles_no-punctuation-and-lower_new


