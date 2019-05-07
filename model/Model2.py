import keras
from keras.utils import plot_model
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, Concatenate, BatchNormalization
from keras import backend as K
from keras.models import Model
from keras.callbacks import ModelCheckpoint
import numpy as np
import matplotlib.pyplot as plt

import os

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['3 Nymphalidae', '4 Lycaenidae']

trainImageDataGen = ImageDataGenerator(rescale=1/255.,
    horizontal_flip=True,
    zoom_range=0.1,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1)

validationImageDataGen = ImageDataGenerator(rescale=1/255.)

# Training data
training_data = os.path.join(root_path, '..', 'data', 'dataset', 'model2', 'train')

# Validation data
validation_data = os.path.join(root_path, '..', 'data', 'dataset', 'model2', 'validation')


trainGen = trainImageDataGen.flow_from_directory(training_data,
	target_size=(224,224),
	batch_size=16,
	class_mode="binary")

valGen = validationImageDataGen.flow_from_directory(validation_data,
	target_size=(224,224),
	batch_size=16,
    class_mode="binary")

