import T6
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

modelbuilder=T6.ModelBuilder(400, 10, 5, True ,'lates-pages-articles_no-punctuation-and-lower_new', 'testkorpora/largetrainedModel400105', 'testkorpora/largetrainedModel400105times.txt')
model = modelbuilder.build()
model.accuracy('../../../Korpora/questions-words.txt')

#enwik9/text__no-punctuation-and-lower
#pages/tech_no-punctuation-and-lower
#lates-pages-articles_no-punctuation-and-lower_new


