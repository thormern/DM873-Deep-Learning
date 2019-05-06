import os
from shutil import copyfile
import uuid

# Gets root path of project
root_path = os.path.dirname(os.path.abspath(__file__))

# Defines folders for where to put the files
folders = ['1 Papilionidae', '2 Pieridae', '3 Nymphalidae', '4 Lycaenidae', '5 Hesperiidae']

# Creates the folders defined above
if not os.path.exists(os.path.join(root_path, 'data', folders[0])):
    os.makedirs(os.path.join(root_path, 'data', folders[0]))

if not os.path.exists(os.path.join(root_path, 'data', folders[1])):
    os.makedirs(os.path.join(root_path, 'data', folders[1]))

if not os.path.exists(os.path.join(root_path, 'data', folders[2])):
    os.makedirs(os.path.join(root_path, 'data', folders[2]))

if not os.path.exists(os.path.join(root_path, 'data', folders[3])):
    os.makedirs(os.path.join(root_path, 'data', folders[3]))

if not os.path.exists(os.path.join(root_path, 'data', folders[4])):
    os.makedirs(os.path.join(root_path, 'data', folders[4]))

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

