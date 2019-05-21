from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

import os
import PIL

datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['3 Nymphalidae', '4 Lycaenidae']

# Training data
training_data = os.path.join(root_path, '..', 'data', 'dataset', 'model2', 'train', folders[0])

if not os.path.exists(training_data):
    os.makedirs(training_data)

preview_folder = os.path.join(root_path, '..', 'data', 'dataset', 'model2','preview')

if not os.path.exists(preview_folder):
            os.makedirs(preview_folder)

_files = [f for f in os.listdir(training_data)]

img = load_img(os.path.join(training_data, _files[0]))  # this is a PIL image
x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

# the .flow() command below generates batches of randomly transformed images
# and saves the results to the `preview/` directory

datagen.flow(x, batch_size=1,
                          save_to_dir=preview_folder, save_prefix='cat', save_format='jpeg')
# i = 0
# for batch in datagen.flow(x, batch_size=1,
#                           save_to_dir=preview_folder, save_prefix='cat', save_format='jpeg'):
#     i += 1
#     if i > 3:
#         break  # otherwise the generator would loop indefinitely