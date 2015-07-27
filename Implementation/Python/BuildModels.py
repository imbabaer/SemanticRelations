'''
In Diesem Skript werden die Modelle erstellt.
'''
import ModelBuilder
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

modelbuilder=ModelBuilder.ModelBuilder(300, 10, 5, True ,'../../Korpora/Wikipedia/pages/tech_no-punctuation-and-lower', 'Models/techModel300105', 'tech300105times.txt')
model = modelbuilder.build()

modelbuilder2=ModelBuilder.ModelBuilder(300, 10, 5, True ,'../../Korpora/Wikipedia/pages/lates-pages-articles_no-punctuation-and-lower', 'Models/largeModel300105', 'large300105times.txt')
model2 = modelbuilder2.build()

'''
#Fuer Tests der Parameter
modelbuilder=ModelBuilder.ModelBuilder(400, 10, 10, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small4001010', 'Models/testkorpora/small4001010times.txt')
model = modelbuilder.build()

modelbuilder=ModelBuilder.ModelBuilder(400, 10, 5, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small400105', 'Models/testkorpora/small400105times.txt')
model = modelbuilder.build()

modelbuilder=ModelBuilder.ModelBuilder(300, 10, 10, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small3001010', 'Models/testkorpora/small3001010times.txt')
model = modelbuilder.build()

modelbuilder=ModelBuilder.ModelBuilder(300, 10, 5, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small300105', 'Models/testkorpora/small300105times.txt')
model = modelbuilder.build()


modelbuilder=ModelBuilder.ModelBuilder(200, 10, 10, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small2001010', 'Models/testkorpora/small2001010times.txt')
model = modelbuilder.build()

modelbuilder=ModelBuilder.ModelBuilder(200, 10, 5, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small200105', 'Models/testkorpora/small200105times.txt')
model = modelbuilder.build()



modelbuilder=ModelBuilder.ModelBuilder(100, 10, 10, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small1001010', 'testkorpora/small1001010times.txt')
model = modelbuilder.build()

modelbuilder=ModelBuilder.ModelBuilder(100, 10, 5, True ,'../../Korpora/Wikipedia/enwik9/enwik9_no-punctuation-and-lower', 'Models/testkorpora/small100105', 'testkorpora/small100105times.txt')
model = modelbuilder.build()

'''