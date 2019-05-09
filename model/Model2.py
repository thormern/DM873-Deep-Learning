from keras.models import load_model
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

# returns a compiled model
# identical to the previous one
model = load_model('model1.h5')

# Freeze the layers except the last layer
# CHANGE THIS TO EXPERIMENT WITH DIFFERENT FROZEN LAYERS
for layer in model.layers[:-1]:
    layer.trainable = False

# Print out model definition
model.summary()

# Check the trainable status of the individual layers
for layer in model.layers:
    print(layer, layer.trainable)

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Training data
training_data = os.path.join(root_path, '..', 'data', 'dataset', 'model2', 'train')

# Validation data
validation_data = os.path.join(root_path, '..', 'data', 'dataset', 'model2', 'validation')

# Data generators, data augmentation for training data
trainImageDataGen = ImageDataGenerator(rescale=1 / 255., horizontal_flip=True)
validationImageDataGen = ImageDataGenerator(rescale=1 / 255.)

trainGen = trainImageDataGen.flow_from_directory(
    training_data,
    target_size=(224, 224),
    batch_size=16,
    class_mode="binary")

valGen = validationImageDataGen.flow_from_directory(
    validation_data,
    target_size=(224, 224),
    batch_size=16,
    class_mode="binary")

# Train model
model.fit_generator(generator=trainGen,
                    epochs=20,
                    steps_per_epoch=10,
                    validation_steps=5,
                    validation_data=valGen)

# Save model
model.save("model2.h5")

# Evaluate model
model.evaluate_generator(valGen, steps=5)
