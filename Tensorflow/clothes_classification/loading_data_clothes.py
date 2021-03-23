import tensorflow as tf 
from tensorflow import keras 
import numpy as np 
import matplotlib.pyplot as plt

data = keras.datasets.fashion_mnist #using keras to load dataset 

(train_images, train_labels), (test_images, test_labels) = data.load_data() #split into train and test data

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat','Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

print(train_images[7])

#right now, the images come in arrays of 28 by 28, and all together, this is a lot of data, we need to condense images onto a scale of 0 and 1, instead of 0 - 255
train_images = train_images / 255.0 #works b/c images are stored in a numpy array
test_images = test_images / 255.0

plt.imshow(train_images[7], cmap=plt.cm.binary)
plt.show()