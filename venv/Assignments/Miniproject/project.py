'''
 * Created by filip on 09/06/2018
'''
import keras

from keras.models import Sequential
from keras.preprocessing import image
from keras.layers import Activation, Dropout, Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import applications

import numpy as np

img_width, img_height = 100,100
data_dir = 'data'
train_data_dir = data_dir + '/training' # REMOVED MOST IMAGES BEFORE UPLOAD FROM DIRECTORY
validation_data_dir = data_dir + '/validation' # REMOVED MOST IMAGES BEFORE UPLOAD FROM DIRECTORY


# train_data_dir = data_dir + '/validation'
# validation_data_dir = data_dir + '/training'

data_generator = image.ImageDataGenerator(
    rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        rescale=1./255,
        shear_range=0.3,
        zoom_range=0.3,
        horizontal_flip=True,
        fill_mode='nearest'
)

validation_data_generator = image.ImageDataGenerator(
        rescale=1./255)

training_data = data_generator.flow_from_directory(
    train_data_dir, target_size=(img_width,img_height), batch_size=100)

# import matplotlib.pyplot as plt
#
# count = 0
# for i in training_data:
#     # png.from_array(i[0][1], "L").save("test.png")
#     plt.imshow(image.array_to_img(i[0][1]))
#     plt.show()
#
#     coount = count +1
#     if (count > 5):
#         break


validation_data = validation_data_generator.flow_from_directory(
    validation_data_dir, target_size=(img_width, img_height), batch_size=100)


input_shape = (img_width, img_height, 3)

training_data_size = 2454
validation_data_size = 826

batch_size = 200

model = Sequential()
model.add(Conv2D(16, (3, 3), input_shape= input_shape))
model.add(Activation('softmax'))
model.add(MaxPooling2D(pool_size=(2)))
#
model.add(Conv2D(16, (3, 3)))
model.add(Activation('softmax'))
# model.add(MaxPooling2D(pool_size=(2)))
#
# model.add(Conv2D(64, (3, 3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2)))
#



# model.add(Flatten(input_shape= input_shape))

model.add(Flatten())
# model.add(Dense(10000))
model.add(Activation('softmax'))


model.add(Dense(128))
model.add(Activation('softmax'))
model.add(Dropout(0.5))
model.add(Dense(5))
model.add(Activation('softmax'))


#

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit_generator(
        training_data,
        steps_per_epoch=training_data_size // batch_size,
        epochs=5,
        # validation_data=validation_data,
        # validation_steps=validation_data_size // batch_size
)





# classes = model.predict_generator(validation_data, 8, True)
# print(classes)

score = model.evaluate_generator(validation_data)
print(score)


model = applications.VGG16(include_top=False, weights='imagenet')

training_data_2 = validation_data_generator.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        batch_size=batch_size,
        class_mode=None,
        shuffle=False)

first_set_features = model.predict_generator(training_data_2, 10)

np.save(open('first_set_weigths.npy', 'wb'), first_set_features)

validation_data_2 = validation_data_generator.flow_from_directory(
        validation_data_dir,
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode=None,
        shuffle=False)

# score = model.evaluate_generator(validation_data)
# print(score)

features_validation = model.predict_generator(validation_data_2, 4)

np.save(open('first_set_weigths_validation.npy', 'wb'), features_validation)


train_data = np.load(open('first_set_weigths.npy', 'rb'))

print(str(train_data))

train_labels = keras.utils.to_categorical(np.array([0] * 400 + [1] * 400 + [2] * 400 + [3] * 400 + [4] * 400), 5)

validation_data = np.load(open('first_set_weigths_validation.npy', 'rb'))


validation_labels = keras.utils.to_categorical(np.array([0] * 160 + [1] * 160 + [2] * 160 + [3] * 160 + [4] * 160), 5)

model = Sequential()
model.add(Flatten(input_shape=train_data.shape[1:]))
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(5))
model.add(Activation('softmax'))


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


model.fit(train_data, train_labels,
          epochs=5,
          batch_size=batch_size,
        )

score = model.evaluate(validation_data, validation_labels)
print(score)

model.save_weights('pretrained_model_with_weights.h5')





# FINE TUNING
# validation_data_generator = ImageDataGenerator(
#         rescale=1./255)
#
# training_data = validation_data_generator.flow_from_directory(
#     train_data_dir, target_size=(img_width,img_height), batch_size=100)
#
# validation_data = validation_data_generator.flow_from_directory(
#     validation_data_dir, target_size=(img_width, img_height), batch_size=100)
#
#
#
#
# model = applications.VGG16(weights='imagenet', include_top=False)
#
# top_model = Sequential()
# top_model.add(Flatten(input_shape=input_shape))
# top_model.add(Dense(64))
# top_model.add(Activation('relu'))
# top_model.add(Dropout(0.5))
# top_model.add(Dense(5))
# top_model.add(Activation('sigmoid'))
#
#
#
# top_model.load_weights('pretrained_model_with_weights.h5')
#
# # add the model on top of the convolutional base
# model.add(top_model)
#
# # set the first 25 layers (up to the last conv block)
# # to non-trainable (weights will not be updated)
# for layer in model.layers[:25]:
#     layer.trainable = False
#
# # compile the model with a SGD/momentum optimizer
# # and a very slow learning rate.
# model.compile(loss='categorical_crossentropy',
#               optimizer=optimizers.SGD(lr=1e-4, momentum=0.9),
#               metrics=['accuracy'])
#
#
# # data_generator = ImageDataGenerator(rotation_range=40,
# #         width_shift_range=0.2,
# #         height_shift_range=0.2,
# #         rescale=1./255,
# #         shear_range=0.2,
# #         zoom_range=0.2,
# #         horizontal_flip=True,
# #         fill_mode='nearest')
#
# validation_data_generator = ImageDataGenerator(
#         rescale=1./255)
#
# training_data = validation_data_generator.flow_from_directory(
#     train_data_dir, target_size=(img_width,img_height), batch_size=100)
#
# validation_data = validation_data_generator.flow_from_directory(
#     validation_data_dir, target_size=(img_width, img_height), batch_size=100)
#
#
#
# # fine-tune the model
# model.fit_generator(
#     training_data,
#     samples_per_epoch=2000,
#     epochs=5,
#     validation_data=validation_data)
