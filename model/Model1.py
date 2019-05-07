import keras
from keras.utils import plot_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, Concatenate, BatchNormalization
from keras import backend as K
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

trainImageDataGen = ImageDataGenerator(rescale=1/255.,horizontal_flip=True)
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


#Test Model in the making - Thor
def create_model( x_train ):

	model = keras.Sequential()

	keras.layers.Conv1D(filters, kernel_size, strides=1, padding='valid', data_format='channels_last', dilation_rate=1,
						activation=None, use_bias=True, kernel_initializer='glorot_uniform', bias_initializer='zeros',
						kernel_regularizer=None, bias_regularizer=None, activity_regularizer=None,
						kernel_constraint=None, bias_constraint=None)
	keras.layers.Dense(units, activation=None, use_bias=True, kernel_initializer='glorot_uniform',
					   bias_initializer='zeros', kernel_regularizer=None, bias_regularizer=None,
					   activity_regularizer=None, kernel_constraint=None, bias_constraint=None)

	keras.layers.MaxPooling2D(pool_size=(2, 2), strides=None, padding='valid', data_format=None)
	keras.layers.Activation(activation)
	keras.layers.Dropout(rate, noise_shape=None, seed=None)
	keras.layers.Flatten(data_format=None)
	optimiser = Adam( lr = 1e-3 )  #hmmm

	model.compile( optimizer = optimiser,
				   loss = 'binary_crossentropy',
				   metrics =[ 'accuracy'] )

	return model

