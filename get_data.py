# 1. Open files 
# 2. slice
# 3. turn valeus into float
# 4. append to list
# 5. turn list to np array
# 6. save np array as train and test

import numpy as np
import csv
from os import walk


def file_to_list(file_names):

	record = []

	for f_name in file_names:

		f = open("data/" + f_name)
		
		for row in f:
			row_floats = []
			sliced = row[:-1].split("\t")
			for sl in sliced:
				row_floats.append(float(sl))

			record.append(row_floats)

	return record


def get_file_names_in_folder(path):
	f = []
	for (dirpath, dirnames, filenames) in walk(path):
	    f.extend(filenames)
	    return sorted(f)

# to not populate training with too similar of data, we may took every nth record
def get_data_sets(path,number_of_training_records,number_of_testing_records,every_nth_record = 1):
	file_names = get_file_names_in_folder(path)

	training_array = np.array(file_to_list(file_names[:number_of_training_records * every_nth_record:every_nth_record]))
	testing_array = np.array(file_to_list(file_names[-1 * number_of_testing_records * every_nth_record::every_nth_record]))

	return training_array,testing_array

if __name__ == "__main__":


	print("Creating data...")
	
	train, test = get_data_sets("./data",500,100,2)

	print("shape of training samples : ", train.shape )
	print("shape of test samples : ", test.shape )
		
	print("-----------------------------------------------------------------")
	print("max values in training : ", train.max(axis=0))
	print("max values in testing : ", test.max(axis=0))
	print("-----------------------------------------------------------------")
	print("min values in training : ", train.min(axis=0))
	print("min values in testing : ", test.min(axis=0))
