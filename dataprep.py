import os
from shutil import copyfile
import uuid
from random import choice, sample
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from PIL import Image
import shutil
import time, sys

######################################## PROGRESSBAR ########################################

# update_progress() : Displays or updates a console progress bar
## Accepts a float between 0 and 1. Any int will be converted to a float.
## A value under 0 represents a 'halt'.
## A value at 1 or bigger represents 100%
def update_progress(imageCount, goal):
    progress = imageCount/goal
    barLength = 25 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress <= 1 and progress > 0:
        status = "Image " + str(imageCount) + " of " + str(goal)
    block = int(round(barLength*progress))
    text = "\rPercent: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), round(progress*100, 2), status)
    sys.stdout.write(text)
    sys.stdout.flush()

######################################## PATH DECLARATION ########################################

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['1 Papilionidae', '2 Pieridae', '3 Nymphalidae', '4 Lycaenidae', '5 Hesperiidae']

# ######################################## DATA DIVITION ########################################

print("\nDeleting existing data..")

# Creates the folders defined above
for folder in folders:
    if os.path.exists(os.path.join(root_path, 'data', folder)):
        shutil.rmtree(os.path.join(root_path, 'data', folder))
    os.makedirs(os.path.join(root_path, 'data', folder))
        

if os.path.exists(os.path.join(root_path, 'data', 'dataset')):
        shutil.rmtree(os.path.join(root_path, 'data', 'dataset'))

print("Deletion completed")

print("\nPreparing for data sampling")
print("Opening file:", root_path, "/data/butterflies.txt")

# Opens and reads the file describing the dataset
f = open(root_path + '/data/butterflies.txt')

print("Reading file..")
lines = f.readlines()
print("File read")

print("Closing file..")
f.close()
print("File closed")

# Goes through each line of the file and copies the file described on that line
# to the folder where it belongs
print("\nDividing base_set into subfolders..")
goal = len(lines)
imageCount = 0
for line in lines:
    imageCount += 1
    update_progress(imageCount, goal)
    columns = line.split()
    src = os.path.join(root_path, 'data/base_set/', columns[0])
    dst = os.path.join(root_path,
                       'data',
                       folders[int(columns[4])-1], 
                       columns[4] + '_' + str(uuid.uuid4()) + '.jpg')
    copyfile(src, dst)
print("\nDivision of base_set complete")

######################################## DATA SAMPLING ########################################

# Helper function which samples randomly and copies samples to destination folder
def sample_data(src, dst, count, _files):

    _data = sample(_files, count)
    _number_of_files = len(_data)

    imageCount = 0
    for _file in _data:
        imageCount += 1
        update_progress(imageCount, _number_of_files)
        _src = os.path.join(src, _file)
        _dst = os.path.join(dst, _file)
        copyfile(_src, _dst)
        _files.remove(_file)
    
    return _files

# ##### MODEL 1 #####
print("\n\n----Creating data for model 1----")
for i in [0,1]:
    #Creates folder
    for _dir in ['validation', 'train']:
        if not os.path.exists(os.path.join(root_path, 'data', 'dataset', 'model1', _dir, folders[i])):
            os.makedirs(os.path.join(root_path, 'data', 'dataset', 'model1', _dir, folders[i]))

    #Creates paths for src and destination of both validation data and training data
    _src = os.path.join(root_path, 'data', folders[i])
    _val_dst = os.path.join(root_path, 'data', 'dataset', 'model1', 'validation', folders[i])
    _train_dst = os.path.join(root_path, 'data', 'dataset', 'model1', 'train', folders[i])
    
    _data = [f for f in os.listdir(_src)]

    print("\nSampling 1000 of ", len(_data), "images from ", folders[i], " for validation..")

    #Calls helper function
    _data = sample_data(_src, _val_dst, 1000, _data) #Validation

    print("\n\nSampling 2000 of ", len(_data), "images from ", folders[i], " for training..")
    sample_data(_src, _train_dst, 2000, _data) #Training

    print("\n")

print("\nDataset for model 1 complete")

# ##### MODEL 2 #####
print("\n\n----Creating data for model 2----")
for i in [2,3]:
    #Creates folder
    for _dir in ['validation', 'train']:
        if not os.path.exists(os.path.join(root_path, 'data', 'dataset', 'model2', _dir, folders[i])):
            os.makedirs(os.path.join(root_path, 'data', 'dataset', 'model2', _dir, folders[i]))

    #Creates paths for src and destination of both validation data and training data
    _src = os.path.join(root_path, 'data', folders[i])
    _val_dst = os.path.join(root_path, 'data', 'dataset', 'model2', 'validation', folders[i])
    _train_dst = os.path.join(root_path, 'data', 'dataset', 'model2', 'train', folders[i])

    _data = [f for f in os.listdir(_src)]

    print("\nSampling 500 of ", len(_data), "images from ", folders[i], " for validation..")

    #Calls helper function
    _data = sample_data(_src, _val_dst, 500, _data) #Validation

    print("\n\nSampling 250 of ", len(_data), "images from ", folders[i], " for training..")
    sample_data(_src, _train_dst, 250, _data) #Training

    print("\n")

print("\nDataset for model 2 complete")

##### MODEL 3 #####
print("\n\n----Creating data for model 3----")
for i in [0,1,2,3,4]:

    desired_number_of_files = 11000

    #Creates paths for src and destination of both validation data and training data
    _src = os.path.join(root_path, 'data', folders[i])
    _val_dst = os.path.join(root_path, 'data', 'dataset', 'model3', 'validation', folders[i])
    _train_dst = os.path.join(root_path, 'data', 'dataset', 'model3', 'train', folders[i])

    model3_data_path = os.path.join(root_path, 'data', 'dataset', 'model3', 'data', folders[i])

    #Creates folder
    for _dir in [_val_dst, _train_dst, model3_data_path]:
        if not os.path.exists(_dir):
            os.makedirs(_dir)

    _files = [name for name in os.listdir(_src)]

    print("\nSampling images for: ", folders[i])
    print("Number of original images: ", len(_files))
    print("Desired minimum number of images: ", desired_number_of_files)

    if (len(_files) < desired_number_of_files):

        print("Generating additional images by transforming original images..")

        datagen = ImageDataGenerator(rotation_range=40,
                                     width_shift_range=0.2,
                                     height_shift_range=0.2,
                                     shear_range=0.2,
                                     zoom_range=0.2,
                                     horizontal_flip=True,
                                     fill_mode='nearest')
        imageCount = 0
        goal = desired_number_of_files - len(_files)
        print("Images to generate: ", goal)
        while imageCount < goal:
            for filename in _files:
                imageCount += 1
                update_progress(imageCount, goal)
                img = load_img(os.path.join(_src, filename))  # this is a PIL image
                img = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
                img = img.reshape((1,) + img.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

                # the .flow() command below generates batches of randomly transformed images
                # and saves the results to the `preview/` directory
                prefix = str(i) + "_" + str(imageCount)
                for batch in datagen.flow(img, batch_size=1,
                                        save_to_dir=model3_data_path, save_prefix=prefix, save_format='jpeg'):
                    break

                if imageCount >= goal:
                    break
            
        print("\nTranformation completed - ", goal, " images was generated")

    print("\nCopying original images..")
    goal = len(_files)
    imageCount = 0
    for _file in _files:
        imageCount += 1
        update_progress(imageCount, goal)
        file_src = os.path.join(_src, _file)
        file_dst = os.path.join(model3_data_path, _file)
        copyfile(file_src, file_dst)
    print("\nCopy complete - ready to sample")

    
    _data = [f for f in os.listdir(model3_data_path)]

    print("\nSampling 2750 of ", len(_data), "images from ", folders[i], " for validation..")

    # Calls helper function
    _data = sample_data(model3_data_path, _val_dst, 2750, _data) #Validation

    print("\n\nSampling 8250 of ", len(_data), "images from ", folders[i], " for training..")

    sample_data(model3_data_path, _train_dst, 8250, _data) #Training

    print("\n")

print("\nDataset for model 3 complete")