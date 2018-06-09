# live coding in class
# from keras.models import Sequential
# from keras.layers import Dense, Activation
# from keras.optimizers import SGD
# import numpy as np
# np.random.seed(123)
#
# lossf='mean_squared_error' #'mean_squared_error'
# actf='sigmoid' #'sigmoid'
# epochs= 100
# mu =0.5
# X_train=np.array([[0,0],[1,0],[0,1],[1,1]])
# if lossf=='categorical_crossentropy':
#     Y_train=np.array([[1, 0],[1, 0],[1, 0],[0, 1]])
# else:
#     Y_train=np.array([[0],[0],[0],[1]])
# X_test=X_train
# Y_test=Y_train
#
# model=Sequential()
# if lossf=='categorical_crossentropy':
#     model.add(Dense(2,batch_input_shape=(None,2),activation=actf))
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
#
# # MLP for XOR
# from keras.models import Sequential
# from keras.layers import Dense, Activation
# from keras.optimizers import SGD
# import numpy as np
# np.random.seed(123)
#
# lossf='mean_squared_error' #'mean_squared_error'
# actf='sigmoid' #'sigmoid'
# epochs= 1000
# mu =0.5
# X_train=np.array([[0,0],[1,0],[0,1],[1,1]])
# if lossf=='categorical_crossentropy':
#     Y_train=np.array([[1, 0],[0, 1],[0, 1],[1, 0]])
# else:
#     Y_train=np.array([[0],[1],[1],[0]])
# X_test=X_train
# Y_test=Y_train
#
# model=Sequential()
# model.add(Dense(2,batch_input_shape=(None,2), activation=actf))
# if lossf=='categorical_crossentropy':
#     model.add(Dense(2,activation=actf))
# else:
#     model.add(Dense(1,activation=actf))
#
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
# from keras.layers import Dense, Activation, Convolution2D, Reshape
#
# (X_train_orig, y_train_orig),(X_test_orig, y_test_orig)=mnist.load_data()
#
# plt.imshow(X_train_orig[3,:,:],cmap='gray_r')
# y_train_orig[3]
#
# X_train=X_train_orig.reshape(X_train_orig.shape[0],28,28,1)
# X_test=X_test_orig.reshape(X_test_orig.shape[0],28,28,1)
# X_train=X_train.astype('float32')
# X_test=X_test.astype('float32')
# X_train=X_train/255
# X_test=X_test/255
# Y_train=np_utils.to_categorical(y_train_orig,10)
# Y_test=np_utils.to_categorical(y_test_orig,10)
#
# K=4
# L=8
# M=12
# N=200
#
# model = Sequential()
#
# stride = 1
# model.add(Conv2D(K,5,5,border_mode='same', input_shape=(28,28,1),
#           activation='relu',subsample=(stride,stride)))
# stride=2
# model.add(Conv2D(L,5,5,border_mode='same', input_shape=(28,28,1),
#           activation='relu',subsample=(stride,stride)))
# stride=2
# model.add(Conv2D(M,4,4,border_mode='same', input_shape=(28,28,1),
#           activation='relu',subsample=(stride,stride)))
# model.add(Reshape(7*7*M))
# model.add(Dense(N,activation='relu'))
# model.add(Dense(10,activation='softmax'))
#
# model.compile(loss='categorical_crossentropy', optimizer='sgd',
#               metrics=['accuracy'])

#
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Conv2D, Reshape, BatchNormalization, Flatten

import numpy as np
np.random.seed(123)  # for reproducibility
from keras.utils import np_utils
from keras.optimizers import Adam
from keras.datasets import mnist
from keras.preprocessing import image
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

# print(Y_test)

K = 4   # first convolutional layer output depth
L = 8   # second convolutional layer output depth
M = 12  # third convolutional layer
N = 200 # fully connected layer

model = Sequential()

stride = 1
model.add(Conv2D(K, 5, padding = "same", input_shape=(28, 28, 1), activation='relu', strides=stride))
stride = 2
model.add(Conv2D(L, 5, padding = "same", activation='relu', strides=stride))
# stride = 2
# model.add(Conv2D(M, 4, padding = "same", activation='relu', strides=stride))

model.add(Flatten())
model.add(Dense(N, activation='relu'))

model.add(Dropout(0.5))
# model.add(BatchNormalization())

model.add(Dense(10, activation='softmax'))

optimizer = Adam(lr=0.03, decay=0.002)
model.compile(loss='categorical_crossentropy',
              optimizer=optimizer,
              metrics=['accuracy'])

model.fit(X_train, Y_train, batch_size=1000, epochs=epochs, verbose=1)

predictions = model.predict(X_test)

biggest_errors = [[0, 0], [0, 0], [0, 0], [0, 0]]

i = 0
while i < len(predictions):
    j = 0
    while j < 10:
        if Y_test[i][j] == 1:

            k = 0
            while k < 4:
                if biggest_errors[k][0] < 1 - predictions[i][j]:
                    biggest_errors[k][0] = 1 - predictions[i][j]
                    biggest_errors[k][1] = i
                    break
                k += 1
        j += 1
    i += 1

for l in biggest_errors:
    plt.imshow(image.array_to_img(X_test[l[1]]))
    plt.show()

smallest_errors = [[1, 0], [1, 0], [1, 0], [1, 0]]

i = 0
while i < len(predictions):
    j = 0
    while j < 10:
        if Y_test[i][j] == 1:

            k = 0
            while k < 4:
                if smallest_errors[k][0] > 1 - predictions[i][j]:
                    smallest_errors[k][0] = 1 - predictions[i][j]
                    smallest_errors[k][1] = i
                    break
                k += 1
        j += 1
    i += 1

for l in smallest_errors:
    plt.imshow(image.array_to_img(X_test[l[1]]))
    plt.show()

# score = model.evaluate(X_test, Y_test, verbose=0)

# print("Score is: " + str(score[1]))

'''
TASK 1

Training with 3 epochs. Dropout method after last fully connected layer. Accuracies shown in table below.

+------------+----------+
| Epoch/Test | Accuracy |
+------------+----------+
| Epoch 1    |   0.8291 |
| Epoch 2    |   0.9601 |
| Epoch 3    |   0.9738 |
| Testing    |   0.98   |
+------------+----------+

TASK 2 and 3 

Training with 1 epoch. Dropout and batch normalisation added after last fully connected layer.

Training accuracy:  0.8943
Test accuracy:      0.971

TASK 4

Trying variations of model architecture, learning rate and activation function. Epochs = 1

+-----------------------------------+---------------+-------------------------------+---------------+
|           Architecture            | Learning rate |      Activation function      | Test accuracy |
+-----------------------------------+---------------+-------------------------------+---------------+
| 1 Convolutional layer,            |               |                               |               |
| dropout(0.2), batch normalisation |        0.003  | ReLU                          |        0.9692 |
|                                   |               |                               |               |
| 1 Convolutional layer,            |               |                               |               |
| dropout(0.2), batch normalisation |        0.003  | Sigmoid                       |        0.5224 |
|                                   |               |                               |               |
| 1 Convolutional layer,            |               |                               |               |
| dropout(0.2), batch normalisation |        0.03   | ReLU                          |        0.9677 |
|                                   |               |                               |               |
| 2 Convolutional layers,           |               |                               |               |
| dropout(0.2), batch normalisation |        0.003  | ReLU(1) + ReLU (2)            |        0.9753 | ***
|                                   |               |                               |               |
| 2 Convolutional layers,           |               |                               |               |
| dropout(0.2), batch normalisation |        0.003  | ReLU(1) + Softmax (2)         |        0.927  |
|                                   |               |                               |               |
| 2 Convolutional layers,           |               |                               |               |
| dropout(0.2), batch normalisation |        0.03   | ReLU(1) + ReLU (2)            |        0.9617 | 
|                                   |               |                               |               |
| 3 Convolutional layers,           |               |                               |               |
| dropout(0.2), batch normalisation |        0.03   | ReLU(1) + ReLU (2) + ReLU (3) |        0.971  |
|                                   |               |                               |               |
| 3 Convolutional layers,           |               |                               |               |
| dropout (0.2)                     |        0.03   | ReLU(1) + ReLU (2) + ReLU (3) |        0.9543 |
|                                   |               |                               |               |
| 3 Convolutional layers,           |               |                               |               |
| dropout (0.5)                     |        0.003  | ReLU(1) + ReLU (2) + ReLU (3) |        0.9529 |
|                                   |               |                               |               |
| 3 Convolutional layers,           |               |                               |               |
| dropout (0.5)                     |        0.03   | ReLU(1) + ReLU (2) + ReLU (3) |        0.9718 | **
|                                   |               |                               |               |
| 3 Convolutional layers,           |               |                               |               |
| dropout (0.5)                     |        0.3    | ReLU(1) + ReLU (2) + ReLU (3) |        0.101  |
+-----------------------------------+---------------+-------------------------------+---------------+

*** and ** indicate best results.

The predictions with biggest errors and predictions with smallest errors are attached at the end of this document.
'''
