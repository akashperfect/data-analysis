import ConfigParser
from os import listdir
from os.path import isfile, join


config = ConfigParser.RawConfigParser()

config.add_section('Data')
config.add_section('Analysis')
config.add_section('Algorithms')
config.add_section('Output')
config.add_section('General')

algo_set = 'KNN,ItemS,LogC'

title =raw_input("Enter title for project: ")
input_dir = raw_input("Enter the path to directory: ")
mapk = raw_input("Enter the Map Calculation Value: ")

onlyfiles = [f for f in listdir(input_dir) if isfile(join(input_dir, f)) and f.endswith(".csv")]

config.set('General', 'title', title)

for file in onlyfiles:
	if("train" in file):
		config.set('Data', 'train', file)
	if("test" in file):
		config.set('Data', 'test', file)

config.set('Data', 'train_data_sf', 'train_data.sf')
config.set('Data', 'test_data_sf', 'test_data.sf')
config.set('Data', 'input_dir', input_dir)
config.set('Analysis', 'pyFile', "analysis.py")
config.set('Output', 'pyFile', "writeToCsv.py")
config.set('Analysis', 'mapk', mapk)
config.set('Algorithms', 'algos', algo_set)
for algo in algo_set.split(','):
	config.set('Algorithms', 'algoFile', algo + ".py")
	config.set('Analysis', 'target_' + algo, title + "_target_" + algo)
	config.set('Analysis', 'prediction_' + algo, title + "_prediction_" + algo)
config.set('Algorithms', 'KNN_Steps', 50000)
config.set('Algorithms', 'file_max_records', 2000)

config.set('Output', 'filename', 'output.csv')

with open('configuration.cfg', 'wb') as configfile:
    config.write(configfile)