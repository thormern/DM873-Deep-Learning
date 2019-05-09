import keras
from keras.utils import plot_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D, Convolution2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, Concatenate, BatchNormalization
from keras import backend as K, Sequential
from keras.models import Model
from keras.callbacks import ModelCheckpoint
from keras import layers

import os

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['1 Papilionidae', '2 Pieridae']

# Training data
training_data = os.path.join(root_path, '..', 'data', 'dataset', 'model1', 'train')

# Validation data
validation_data = os.path.join(root_path, '..', 'data', 'dataset', 'model1', 'validation')

# Data generators, data augmentation for training data
trainImageDataGen = ImageDataGenerator(rescale=1/255.,horizontal_flip=True, rotation_range=25, width_shift_range=10,
                                       height_shift_range=10, vertical_flip=True)
validationImageDataGen = ImageDataGenerator(rescale=1/255.)

trainGen = trainImageDataGen.flow_from_directory(
	training_data,
	target_size=(224,224),
	batch_size=16,
	class_mode="binary")

valGen = validationImageDataGen.flow_from_directory(
	validation_data,
	target_size=(224,224),
	batch_size=16,
	class_mode="binary")


# Model definition
# CHANGE THIS TO TEST DIFFERENT MODELS
IMG_SIZE = 224
model = Sequential()
model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Convolution2D(32, 3, 3, activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 3)))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())
model.add(Dense(1, activation='softmax'))

# Print out model definition
model.summary()

# Prepare the model for training
model.compile(loss='binary_crossentropy', optimizer='adam')

# Train the model
model.fit_generator(generator=trainGen,
					epochs=20,
					steps_per_epoch=10,
					validation_steps=5,
                    validation_data=valGen)

# Save the model
model.save("model1.h5")

# Evaluate the model
model.evaluate_generator(valGen, steps=5)
