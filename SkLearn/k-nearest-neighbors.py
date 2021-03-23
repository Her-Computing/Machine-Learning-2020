import pandas as pd
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import numpy as numpy
from sklearn import linear_model, preprocessing
import pickle

"""
K-Nearest Neighbors - Classificiation Algorithm
	Algoritham that takes in an integer k and a test value. The algorithm relies upon 2 classes, which are
	generated from analysis of the dataset. The algorithm takes in the test value and places it in the 
	middle of the graph. Then, based on the number k, the algorithm will draw a circle around the test
	value until k amount of class reps are included in the circle. Next, the algorithm looks at the 
	reps and tallies the number from each class. Whichever class has a majority is the class that is
	classified to the test value.

	In other situations, the algorithm will split the graph into different parts, where each part is 
	associated to a certain class value

	Good Practices:
		k must always be an odd to prevent ties
		Always use features that only have numerical values - may need to convert non-nunmerical data into numerical data
"""

"""
Predicting if car purchose is good or not based off factors
"""

data = pd.read_csv("Datasets/car.data")

#clean up data
le = preprocessing.LabelEncoder()
buying = le.fit_transform(list(data["buying"]))
maint = le.fit_transform(list(data["maint"]))
door = le.fit_transform(list(data["door"]))
persons = le.fit_transform(list(data["persons"]))
lug_boot = le.fit_transform(list(data["lug_boot"]))
safety = le.fit_transform(list(data["safety"]))
cls = le.fit_transform(list(data["class"]))

predict = "class"

X = list(zip(buying, maint, door, persons, lug_boot, safety))
y = list(cls)

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size = 0.1)

model = KNeighborsClassifier(n_neighbors=9)

model.fit(x_train, y_train)
acc = model.score(x_test, y_test)
print(acc)

predicted = model.predict(x_test)
names = ["unacc", "acc", "good", "vgood"]

for x in range(len(predicted)):
    print("Predicted: ", names[predicted[x]], "Data: ", x_test[x], "Actual: ", names[y_test[x]])
    """
    return to us  an array with the index in our data of each neighbor. 
    If distance=True then it will also return the distance to each neighbor from our data point.

    n = model.kneighbors([x_test[x]], 9, True)
    print("N: ", n)
    """