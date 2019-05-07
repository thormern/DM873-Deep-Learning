import os
from shutil import copyfile
import uuid
from random import choice, sample

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['1 Papilionidae', '2 Pieridae', '3 Nymphalidae', '4 Lycaenidae', '5 Hesperiidae']

######################################## DATA DIVITION ########################################

# Creates the folders defined above
for folder in folders:
    if not os.path.exists(os.path.join(root_path, 'data', folder)):
        os.makedirs(os.path.join(root_path, 'data', folder))

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
def sample_data(src, dst, count):
    _files = [f for f in os.listdir(src)]

    _data = sample(_files, count)

    for _file in _data:
        _src = os.path.join(src, _file)
        _dst = os.path.join(dst, _file)
        copyfile(_src, _dst)

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

    #Calls helper function
    sample_data(_src, _val_dst, 1000) #Validation
    sample_data(_src, _train_dst, 2000) #Training

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

    #Calls helper function
    sample_data(_src, _val_dst, 500) #Validation
    sample_data(_src, _train_dst, 250) #Training

##### MODEL 3 #####
for i in [0, 1, 2, 3, 4]:
    #Creates folder
    for _dir in ['validation', 'train']:
        if not os.path.exists(os.path.join(root_path, 'data', 'dataset', 'model3', _dir, folders[i])):
            os.makedirs(os.path.join(root_path, 'data', 'dataset', 'model3', _dir, folders[i]))

    #Creates paths for src and destination of both validation data and training data
    _src = os.path.join(root_path, 'data', folders[i])
    _val_dst = os.path.join(root_path, 'data', 'dataset', 'model3', 'validation', folders[i])
    _train_dst = os.path.join(root_path, 'data', 'dataset', 'model3', 'train', folders[i])

    #Calls helper function
    sample_data(_src, _val_dst, 700) #Validation
    sample_data(_src, _train_dst, 1000) #Training