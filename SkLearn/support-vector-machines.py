import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

'''
Support Vector Machines - classification algo

Generates a line called a hyperplane that is a line that acts as a boundary for the 2 classes.
For every d-dimensions, the hyperplane is d-1 dimensions. The distance between the 2 closest
points from each class is maximized when drawing a hyperplane. 

When data of 2 classes is scattered: We can use a kernel (function) to transform the graph 
into another dimension. This can help with drawing the hyperplane. Kernel Function examples:
f(x) = x* y, etc. Kernel returns dot product of vectors (multiplying 2 vectors). Kernel also helps 
with reducing computational space usage. 

Pro: effective in high dimensional spaces, easy to use
Con: will return bad results in there is not enough data

Soft margin: hyperplane line where the parts may have vals of both classes, can improve classification
hard magin: opposite of a soft margin
'''

cancer = datasets.load_breast_cancer()

#print(cancer.feature_names)
#print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.2)

clf = svm.SVC(kernel="linear") #applying kernel
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

names = ["malignant", "benign"]
for x in range(len(y_pred)):
	print("Predicted: ", names[y_pred[x]])

acc = metrics.accuracy_score(y_test, y_pred)

print(acc)