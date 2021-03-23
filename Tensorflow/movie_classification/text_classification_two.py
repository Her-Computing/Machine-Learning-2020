import tensorflow as tf
from tensorflow import keras
import numpy as np

data = keras.datasets.imdb

(train_data, train_labels), (test_data, test_labels) = data.load_data(num_words=88000)

print(train_data)

word_index = data.get_word_index() 

word_index = {k:(v+3) for k, v in word_index.items()}
word_index["<PAD>"] = 0
word_index["<START>"] = 1
word_index["<UNK>"] = 2
word_index["<UNUSED>"] = 3

reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])

largest_rating = 0
rating_length = np.arange(len(train_data))
for i in range(len(train_data)):
	rating_length[i] = len(train_data[i])

	if rating_length[i] > largest_rating:
		largest_rating = rating_length[i]

def decode_review(text):
	return " ".join([reverse_word_index.get(i, "?") for i in text])

print(decode_review(test_data[0]))
print(len(test_data[0]))
print(len(test_data[1]))

train_data = keras.preprocessing.sequence.pad_sequences(train_data, value=word_index["<PAD>"], padding="post", maxlen=largest_rating)
test_data = keras.preprocessing.sequence.pad_sequences(test_data, value=word_index["<PAD>"], padding="post", maxlen=largest_rating)

print("\n\n\n\n", len(test_data[0]))
print(len(test_data[1]))