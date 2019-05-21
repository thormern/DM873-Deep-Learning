import os
from shutil import copyfile
import uuid
from random import choice, sample
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import PIL
import shutil

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['1 Papilionidae', '2 Pieridae', '3 Nymphalidae', '4 Lycaenidae', '5 Hesperiidae']

######################################## DATA DIVITION ########################################

# Creates the folders defined above
for folder in folders:
    if os.path.exists(os.path.join(root_path, 'data', folder)):
        shutil.rmtree(os.path.join(root_path, 'data', folder))
    os.makedirs(os.path.join(root_path, 'data', folder))
        

if os.path.exists(os.path.join(root_path, 'data', 'dataset')):
        shutil.rmtree(os.path.join(root_path, 'data', 'dataset'))

# Opens and reads the file describing the dataset
f = open(root_path + '/data/butterflies.txt')
lines = f.readlines()
f.close()

# Goes through each line of the file and copies the file described on that line
# to the folder where it belongs
for line in lines:
    columns = line.split()
    src = os.path.join(root_path, 'data/base_set/', columns[0])
    dst = os.path.join(root_path,
                       'data',
                       folders[int(columns[4])-1], 
                       columns[4] + '_' + str(uuid.uuid4()) + '.jpg')
    copyfile(src, dst)


######################################## DATA SAMPLING ########################################

#Helper function which samples randomly and copies samples to destination folder
def sample_data(src, dst, count, _files):

    # _files = [f for f in os.listdir(src)]

    _data = sample(_files, count)
    _number_of_files = len(_data)

    for _file in _data:
        _src = os.path.join(src, _file)
        _dst = os.path.join(dst, _file)
        copyfile(_src, _dst)
        _files.remove(_file)
    
    return _files

##### MODEL 1 #####
for i in [0,1]:
    #Creates folder
    for _dir in ['validation', 'train']:
        if not os.path.exists(os.path.join(root_path, 'data', 'dataset', 'model1', _dir, folders[i])):
            os.makedirs(os.path.join(root_path, 'data', 'dataset', 'model1', _dir, folders[i]))

    #Creates paths for src and destination of both validation data and training data
    _src = os.path.join(root_path, 'data', folders[i])
    _val_dst = os.path.join(root_path, 'data', 'dataset', 'model1', 'validation', folders[i])
    _train_dst = os.path.join(root_path, 'data', 'dataset', 'model1', 'train', folders[i])
    
    _files = [f for f in os.listdir(_src)]

    #Calls helper function
    _data = sample_data(_src, _val_dst, 1000, _files) #Validation

    sample_data(_src, _train_dst, 2000, _data) #Training

##### MODEL 2 #####
for i in [2,3]:
    #Creates folder
    for _dir in ['validation', 'train']:
        if not os.path.exists(os.path.join(root_path, 'data', 'dataset', 'model2', _dir, folders[i])):
            os.makedirs(os.path.join(root_path, 'data', 'dataset', 'model2', _dir, folders[i]))

    #Creates paths for src and destination of both validation data and training data
    _src = os.path.join(root_path, 'data', folders[i])
    _val_dst = os.path.join(root_path, 'data', 'dataset', 'model2', 'validation', folders[i])
    _train_dst = os.path.join(root_path, 'data', 'dataset', 'model2', 'train', folders[i])

    _files = [f for f in os.listdir(_src)]

    #Calls helper function
    _data = sample_data(_src, _val_dst, 500, _files) #Validation
    sample_data(_src, _train_dst, 250, _data) #Training

# ##### MODEL 3 #####
# for i in [0]:

#     desired_number_of_files = 11000

#     #Creates paths for src and destination of both validation data and training data
#     _src = os.path.join(root_path, 'data', folders[i])
#     _val_dst = os.path.join(root_path, 'data', 'dataset', 'model3', 'validation', folders[i])
#     _train_dst = os.path.join(root_path, 'data', 'dataset', 'model3', 'train', folders[i])

#     model3_data_path = os.path.join(root_path, 'data', 'dataset', 'model3', 'data', folders[i])

#     #Creates folder
#     for _dir in [_val_dst, _train_dst, model3_data_path]:
#         if not os.path.exists(_dir):
#             os.makedirs(_dir)

#     _files = [name for name in os.listdir(_src)]

#     if (len(_files) < desired_number_of_files):
#         datagen = ImageDataGenerator(rotation_range=40,
#                                      width_shift_range=0.2,
#                                      height_shift_range=0.2,
#                                      shear_range=0.2,
#                                      zoom_range=0.2,
#                                      horizontal_flip=True,
#                                      fill_mode='nearest')
        
#         # _temp_data = sample(_files, desired_number_of_files)

#         for filename in _files:

#             img = load_img(os.path.join(_src, filename))  # this is a PIL image
#             x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
#             x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

#             # the .flow() command below generates batches of randomly transformed images
#             # and saves the results to the `preview/` directory

#             # datagen.flow(x, batch_size=1,
#             #                         save_to_dir=model3_data_path, save_prefix='cat', save_format='jpeg')

#             j = 0
#             for batch in datagen.flow(x, batch_size=1,
#                                     save_to_dir=model3_data_path, save_prefix='cat', save_format='jpeg'):
#                 j += 1
#                 if i > (desired_number_of_files - len(_files))/len(_files):
#                     break  # otherwise the generator would loop indefinitely



#     #Creates folder
#     # for _dir in ['validation', 'train']:
#     #     if not os.path.exists(os.path.join(root_path, 'data', 'dataset', 'model3', _dir, folders[i])):
#     #         os.makedirs(os.path.join(root_path, 'data', 'dataset', 'model3', _dir, folders[i]))

#     #Calls helper function
#     # sample_data(_src, _val_dst, 700) #Validation
#     # sample_data(_src, _train_dst, 1000) #Training