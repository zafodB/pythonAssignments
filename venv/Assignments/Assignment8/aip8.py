featsort=np.sort(preds[0,:])
plt.plot(featsort[0:997])

#
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Activation, Dropout, Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
import numpy as np
import os

img_width, img_height = 150,150
data_dir='cats_dogs_small/cats_dogs_small/' # hp mac
train_data_dir = data_dir + 'train'
validation_data_dir = data_dir +  'validation'
nb_train_samples=2000
nb_validation_samples=800
epochs = 1
batch_size= 16

if K.image_data_format() == 'channels_first':
    input_shape =(3,img_width,img_height)
else:
    input_shape = (img_width, img_height,3)

model = Sequential()
model.add(Conv2D(32,(3,3),input_shape=input_shape))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(32,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64,(3,3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
               optimizer='rmsprop',
               metrics=['accuracy'])

train_datagen = ImageDataGenerator(
        rescale =1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale =1./255)

train_generator=train_datagen.flow_from_directory(
    train_data_dir,target_size=(img_width,img_height),
batch_size=batch_size,class_mode='binary' )

validation_generator=test_datagen.flow_from_directory(
    validation_data_dir,target_size=(img_width,img_height),
batch_size=batch_size,class_mode='binary' )

model.fit_generator(train_generator,
                steps_per_epoch=nb_train_samples // batch_size,
                    epochs=epochs,
                    validation_data=validation_generator,
                    validation_steps=nb_validation_samples // batch_size,
                    )

# ##
#
# # aip live coding in class
# # Windows: Pillow
# # more structured detailed version of the coding in class also in the Dropbox:
# # data_augmentation.py: Data preparation through geometric
# #            operations
# # inceptionV3predict.py: Elephant recognition with a pretrained
# #           InceptionV3 network
# # training_cats.py: Convnet for full training of Cats vs. Dogs
# # get_bottleneck_fc_model.py: replacing the
# #       last fully connected layers of a VGG16
# # retrainVGG16.py: finetuning last conv layers
# # All examples are commented in detail on this blog
# # https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
# from keras.preprocessing.image import ImageDataGenerator, \
#     array_to_img, img_to_array, load_img
#
# datagen = ImageDataGenerator(
#     rotation_range=40,
#     width_shift_range=0.2,
#     height_shift_range=0.2,
#     shear_range=0.2,
#     zoom_range=0.2,
#     horizontal_flip=True,
#     fill_mode='nearest')
# data_dir='cats_dogs_small/cats_dogs_small/'
# img = load_img(data_dir + 'train/cats/cat.0.jpg')
# x = img_to_array(img) # (3, 150, 150)
# x = x.reshape((1,)+x.shape)# (1,3, 150, 150)
#
# i= 0
# for batch in datagen.flow(x, batch_size=1,
#                           save_to_dir='preview',
#                           save_prefix='cat',
#                           save_format='jpeg'):
#     i +=1
#     if i>20:
#         break


# from keras.applications.inception_v3 import InceptionV3
# from keras.preprocessing import image
# from keras.applications.inception_v3 import \
#     preprocess_input, decode_predictions
# import numpy as np
#
# model = InceptionV3(weights='imagenet')
#
# img_path='african-elephant-bull.jpg'
# img = image.load_img(img_path, target_size=(299,299))
# x = image.img_to_array(img)
# x = np.expand_dims(x,axis=0)
# x = preprocess_input(x)
#
# preds=model.predict(x)
#
# print('Predicted:',decode_predictions(preds,top=3)[0])
#
# import matplotlib.pyplot as plt
# # preds[0,:]
# plt.plot(preds[0,:])
from keras.models import Sequential
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Activation, Dropout, Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import applications

import numpy as np


img_width, img_height = 150,150
data_dir='cats_dogs_small/cats_dogs_small/' # hp mac
train_data_dir = data_dir + 'train'
validation_data_dir = data_dir +  'validation'
nb_train_samples=2000
nb_validation_samples=800
epochs = 1
batch_size= 16
datagen = ImageDataGenerator(
        rescale =1./255)

model= applications.VGG16(include_top=False, weights='imagenet')


generator=datagen.flow_from_directory(
    train_data_dir,target_size=(img_width,img_height),
batch_size=batch_size,class_mode=None, shuffle=False)

bottleneck_features_train=model.predict_generator(
    generator,nb_train_samples // batch_size)

np.save('bottleneck_features_train.npy',bottleneck_features_train)

generator=datagen.flow_from_directory(
    validation_data_dir,target_size=(img_width,img_height),
batch_size=batch_size,class_mode=None, shuffle=False)

bottleneck_features_validation=model.predict_generator(
    generator,nb_validation_samples // batch_size)

np.save('bottleneck_features_validation.npy',bottleneck_features_validation)


train_data=np.load('bottleneck_features_train.npy')

train_labels= np.array([0]*(nb_train_samples // 2)
                       +[1]*(nb_train_samples // 2))

validation_data=np.load('bottleneck_features_validation.npy')

validation_labels= np.array([0]*(nb_validation_samples // 2)
                       +[1]*(nb_validation_samples // 2))

model=Sequential()
model.add(Flatten(input_shape=train_data.shape[1:]))
model.add(Dense(256,activation='relu'))
model.add(Dropout(.5))
model.add(Dense(1,activation='sigmoid'))



model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(train_data, train_labels,
          epochs=epochs,
          batch_size=batch_size,
          validation_data=(validation_data,validation_labels)
          )

model.save_weights('bottleneck_fc_model.h5')


