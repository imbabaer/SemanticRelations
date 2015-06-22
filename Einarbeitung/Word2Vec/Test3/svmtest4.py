from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.datasets import fetch_20newsgroups
import numpy as np
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']


twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
text_clf = Pipeline([('vect', CountVectorizer()),
                     ('tfidf', TfidfTransformer()),
                     ('clf', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, n_iter=5, random_state=42)),
])

print type(twenty_train.data)
print type(twenty_train.target)
print len(twenty_train.data)
print len(twenty_train.target)
print twenty_train.data[:2]
_ = text_clf.fit(twenty_train.data, twenty_train.target)
twenty_test = fetch_20newsgroups(subset='test',categories=categories, shuffle=True, random_state=42)
docs_test = twenty_test.data
predicted = text_clf.predict(docs_test)
#print np.mean(predicted == twenty_test.target)
print text_clf.predict(docs_test[51])

from sklearn import metrics
#print(metrics.classification_report(twenty_test.target, predicted,target_names=twenty_test.target_names))