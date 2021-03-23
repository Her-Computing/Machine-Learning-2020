#without kernel - acc is 5% less

import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()

#print(cancer.feature_names)
#print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

clf = svm.SVC()
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test) # Predict values for our test data

acc = metrics.accuracy_score(y_test, y_pred) # Test them against our correct values
print(acc)
print(y_pred)