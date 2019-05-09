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

trainImageDataGen = ImageDataGenerator(rescale=1/255.,horizontal_flip=True, rotation_range=25, width_shift_range=10,
                                       height_shift_range=10, vertical_flip=True)
validationImageDataGen = ImageDataGenerator(rescale=1/255.)
IMG_SIZE = 224
batch_size = 32
trainGen = trainImageDataGen.flow_from_directory(
	training_data,
	target_size=(224,224),
	batch_size=batch_size,
	class_mode="binary")

valGen = validationImageDataGen.flow_from_directory(
	validation_data,
	target_size=(224,224),
	batch_size=batch_size,
	class_mode="binary")




inputLayer = Input(shape=(IMG_SIZE,IMG_SIZE,3))

conv2D_1 = Convolution2D(32, kernel_size=(1,1), activation='relu')(inputLayer)
conv2D_2 = Convolution2D(32, kernel_size=(3,3), activation='relu')(inputLayer)
conv2D_3 = Convolution2D(32, kernel_size=(5,5), activation='relu')(inputLayer)
maxPool_1 = MaxPooling2D(pool_size=(3,3))(inputLayer)

flat_1 = Flatten()(conv2D_1)
flat_2 = Flatten()(conv2D_2)
flat_3 = Flatten()(conv2D_3)
flat_4 = Flatten()(maxPool_1)

concatenate_1 = Concatenate()([flat_1, flat_2, flat_3, flat_4])


outputLayer = Dense(1, activation='softmax')(concatenate_1)

model = Model(inputLayer, outputLayer)

model.summary()
model.compile(loss='binary_crossentropy', optimizer='adam')
model.fit_generator(generator=trainGen,
					epochs=10,
					steps_per_epoch=10,
					validation_steps=5,
                    validation_data=valGen)
model.save("model1.h5")
model.evaluate_generator(valGen, steps=5)
