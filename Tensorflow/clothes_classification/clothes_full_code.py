import tensorflow as tf 
from tensorflow import keras 
import numpy as np 
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist #using keras to load dataset 

(train_images, train_labels), (test_images, test_labels) = data.load_data() #split into train and test data

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#right now, the images come in arrays of 28 by 28, and all together, this is a lot of data, we need to condense images onto a scale of 0 and 1, instead of 0 - 255
train_images = train_images / 255.0 #works b/c images are stored in a numpy array
test_images = test_images / 255.0

#however, nueron will not be able to accurately process a 28 by 28 array, so we need to flatten the array and make it 1-D, now array will have 784 indexes 
model = keras.Sequential([
	keras.layers.Flatten(input_shape = (28, 28)),
	keras.layers.Dense(128 , activation = "relu"), #dense means connect all nuerons from previous layer, activation is for activation layer
	keras.layers.Dense(10, activation = "softmax") #softmax is probability of answer being right 
])

model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])
model.fit(train_images, train_labels, epochs = 13) #epochs mean how many times will the model see the info passed in 0

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("accuracy", test_acc)

predictions = model.predict(test_images)

'''
for i in range (15):

	plt.grid(False)
	plt.imshow(train_images[i], cmap = plt.cm.binary)
	plt.xlabel("actual: " + class_names[test_labels[i]])
	plt.title("prediction: "+ class_names[np.argmax(prediction[i])]) #predictions are percentages that the model thinks correspond to the classes
'''

def plot_image(i, predictions_array, true_label, img):
  predictions_array, true_label, im g= predictions_array, true_label[i], img[i]
  plt.grid(False)
  plt.xticks([])
  plt.yticks([])

  plt.imshow(img, cmap=plt.cm.binary)

  predicted_label = np.argmax(predictions_array)
  if predicted_label == true_label:
    color = 'blue'
  else:
    color = 'red'

  plt.xlabel("{} {}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])  
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')

for i in range(15):
	plt.figure(figsize=(6,3))
	plt.subplot(1,2,1)
	plot_image(i, predictions[i], test_labels, test_images)
	plt.subplot(1,2,2)
	plot_value_array(i, predictions[i],  test_labels)
	plt.show()

'''
plt.figure(figsize=(5,5))
for i in range(5):
    plt.grid(False)
    plt.imshow(test_images[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[test_labels[i]])
    plt.title(class_names[np.argmax(predictions[i])])
    plt.show()
'''