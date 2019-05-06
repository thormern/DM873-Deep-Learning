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

trainImageDataGen = ImageDataGenerator(rescale=1/255.,
    horizontal_flip=True,
    zoom_range=0.1,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1)

validationImageDataGen = ImageDataGenerator(rescale=1/255.)

trainGen = trainImageDataGen.flow_from_directory("Project/Task2/Train",
	target_size=(224,224),
	batch_size=16,
	class_mode="binary")

valGen = validationImageDataGen.flow_from_directory("Project/Task2/Validation",
	target_size=(224,224),
	batch_size=16,
    class_mode="binary")


image_path = "Project/Task2/Train/3 Nymphalidae/4.jpg"
image = plt.imread(image_path).astype(float)

save_here = "Project/Task2/Augmentation/1.png"
trainGen.fit(image)
trainGen.flow(image,                    #image we chose
        save_to_dir=save_here,     #this is where we figure out where to save
        save_prefix='aug',        # it will save the images as 'aug_0912' some number for every new augmented image
        save_format='png')    # here we define a range because we want 10 augmented images otherwise it will keep looping forever I think
    