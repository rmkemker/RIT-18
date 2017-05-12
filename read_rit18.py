"""
Name: read_rit18.py
Author: Ronald Kemker
Description: This loads all of the data in the RIT-18 dataset.  

Note:
See paper for details: https://arxiv.org/abs/1703.01918
"""


from scipy.io import loadmat

file_path = 'rit18_data.mat'

dataset = loadmat(file_path)

#Load Training Data and Labels
train_data = dataset['train_data']
train_mask = train_data[-1]
train_data = train_data[:6]
train_labels = dataset['train_labels']

#Load Validation Data and Labels
val_data = dataset['val_data']
val_mask = val_data[-1]
val_data = val_data[:6]
val_labels = dataset['val_labels']

#Load Test Data
test_data = dataset['test_data']
test_mask = test_data[-1]
test_data = test_data[:6]

band_centers = dataset['band_centers'][0]
band_center_units = dataset['band_center_units']
classes = dataset['classes']                          

#Print some info about the dataset
print(dataset['sensor'][0])
print(dataset['info'][0])