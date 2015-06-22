from sklearn import svm
X = [[0, 0], [1, 1],[2,2]]
y = [0, 1, 12]
clf = svm.SVC()
clf.fit(X, y)
print clf.predict([[2., 2.]])