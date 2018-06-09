# # live coding in class
# from keras.models import Sequential
# from keras.layers import Dense, Activation
# from keras.optimizers import SGD
# import numpy as np
#
# np.random.seed(123)
#
# lossf = 'mean_squared_error'  # 'mean_squared_error'
# actf = 'sigmoid'  # 'sigmoid'
# epochs = 100
# mu = 0.5
# X_train = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
# if lossf == 'categorical_crossentropy':
#     Y_train = np.array([[1, 0], [1, 0], [1, 0], [0, 1]])
# else:
#     Y_train = np.array([[0], [0], [0], [1]])
# X_test = X_train
# Y_test = Y_train
#
# model = Sequential()
# if lossf == 'categorical_crossentropy':
#     model.add(Dense(2, batch_input_shape=(None, 2), activation=actf))
# else:
#     model.add(Dense(1, batch_input_shape=(None, 2), activation=actf))
#
# sgd = SGD(lr=mu, decay=0.0)
# model.compile(loss=lossf,
#               optimizer=sgd,
#               metrics=['accuracy'])
#
# model.fit(X_train, Y_train, batch_size=1, epochs=epochs, verbose=1)
#
# # MLP for XOR
# from keras.models import Sequential
# from keras.layers import Dense, Activation
# from keras.optimizers import SGD
# import numpy as np
#
# np.random.seed(123)
#
# lossf = 'mean_squared_error'  # 'mean_squared_error'
# actf = 'sigmoid'  # 'sigmoid'
# epochs = 1000
# mu = 0.5
# X_train = np.array([[0, 0], [1, 0], [0, 1], [1, 1]])
# if lossf == 'categorical_crossentropy':
#     Y_train = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])
# else:
#     Y_train = np.array([[0], [1], [1], [0]])
# X_test = X_train
# Y_test = Y_train
#
# model = Sequential()
# model.add(Dense(2, batch_input_shape=(None, 2), activation=actf))
# if lossf == 'categorical_crossentropy':
#     model.add(Dense(2, activation=actf))
# else:
#     model.add(Dense(1, activation=actf))
#
# sgd = SGD(lr=mu, decay=0.0)
# model.compile(loss=lossf,
#               optimizer=sgd,
#               metrics=['accuracy'])
#
# model.fit(X_train, Y_train, batch_size=1, epochs=epochs, verbose=1)
# # reading images
#
# from keras.datasets import mnist
# from keras.models import Sequential
# from keras.utils import np_utils
# import matplotlib.pyplot as plt
# from keras.layers import Dense, Activation, Conv2D, Flatten
#
# (X_train_orig, y_train_orig), (X_test_orig, y_test_orig) = mnist.load_data()
#
# plt.imshow(X_train_orig[3, :, :], cmap='gray_r')
# y_train_orig[3]
#
# X_train = X_train_orig.reshape(X_train_orig.shape[0], 28, 28, 1)
# X_test = X_test_orig.reshape(X_test_orig.shape[0], 28, 28, 1)
# X_train = X_train.astype('float32')
# X_test = X_test.astype('float32')
# X_train = X_train / 255
# X_test = X_test / 255
# Y_train = np_utils.to_categorical(y_train_orig, 10)
# Y_test = np_utils.to_categorical(y_test_orig, 10)
#
# K = 4
# L = 8
# M = 12
# N = 200
#
# model = Sequential()
#
# stride = 1
# model.add(Conv2D(K, 5, padding='same', input_shape=(28, 28, 1),
#                         activation='relu', strides=(stride, stride)))
# stride = 2
# model.add(Conv2D(L, 5, padding='same', input_shape=(28, 28, 1),
#                         activation='relu', strides=(stride, stride)))
# stride = 2
# model.add(Conv2D(M, 4, padding='same', input_shape=(28, 28, 1),
#                         activation='relu', strides=(stride, stride)))
# model.add(Flatten())
# model.add(Dense(N, activation='relu'))
# model.add(Dense(10, activation='softmax'))
#
# model.compile(loss='categorical_crossentropy', optimizer='sgd',
#               metrics=['accuracy'])

#
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, BatchNormalization, Conv2D, Flatten, Reshape

import numpy as np

np.random.seed(123)  # for reproducibility
from keras.utils import np_utils
from keras.optimizers import Adam
from keras.datasets import mnist

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt


epochs = 1

# Load pre-shuffled MNIST data into train and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Preprocess input data
X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Preprocess class labels
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)

K = 4  # first convolutional layer output depth
L = 8  # second convolutional layer output depth
M = 12  # third convolutional layer
N = 200  # fully connected layer

model = Sequential()

stride = 1
model.add(Conv2D(K, 5, padding='same', input_shape=(28, 28, 1), activation='relu', strides = (stride, stride)))
stride = 2
    model.add(Conv2D(L, 5, padding='same', activation='relu', strides=(stride, stride), input_shape=(28, 28, 4)))
stride = 2
model.add(Conv2D(M, 5, padding='same', activation='relu', strides=(stride, stride), input_shape=(14, 14, 8)))
model.add(Flatten())
model.add(Dense(N, activation='relu'))
model.add(Dropout(0.4))
model.add(BatchNormalization(momentum=0.1))
model.add(Dense(10, activation='softmax'))

optimizer = Adam(lr=0.003, decay=0.002)
model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=1000, epochs=epochs, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=0)
print("score: "+str(score[1]))

#[0.14895800674855708, 0.954]
#[0.16104559338390828, 0.9536]

# score: [0.05180156317660585, 0.9834]

objects = ('Model 1', 'Model 2')
y_pos = np.arange(len(objects))
performance = [score[1], score[1]-0.5]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Probability')
plt.title('Model probabilities')

plt.show()
