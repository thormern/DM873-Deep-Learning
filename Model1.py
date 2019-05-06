import keras
from keras.utils import plot_model
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense, Input, Concatenate, BatchNormalization
from keras import backend as K
from keras.models import Model
from keras.callbacks import ModelCheckpoint

trainImageDataGen = ImageDataGenerator(rescale=1/255.,horizontal_flip=True)
validationImageDataGen = ImageDataGenerator(rescale=1/255.)

trainGen = trainImageDataGen.flow_from_directory("Project/Task1/Train",
	target_size=(224,224),
	batch_size=16,
	class_mode="binary")

valGen = validationImageDataGen.flow_from_directory("Project/Task1/Validation",
	target_size=(224,224),
	batch_size=16,
    class_mode="binary")

	