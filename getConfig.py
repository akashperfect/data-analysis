import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('configuration.cfg')

def addPath(fileName):
	global path
	return path + fileName

conf = dict()
title = conf['title'] = config.get('General', 'title')
conf['path'] = config.get('Data', 'input_dir')
path = conf['path'] + "/"
conf['train_data'] = addPath(config.get('Data', 'train'))
conf['test_data'] = addPath(config.get('Data', 'test'))
conf['mapk'] = config.get('Analysis', 'mapk')
conf['output'] = addPath(config.get('Output', 'filename'))
algos_set = config.get('Algorithms', 'algos').split(',')
conf['algo_set'] = algos_set
conf['analysisPy'] = addPath(config.get('Analysis', 'pyFile'))
conf['OutputPy'] = addPath(config.get('Output', 'pyFile'))


for algo in algos_set:
	conf['algoFile'] = config.get('Algorithms', 'algoFile')
	conf[algo] = {'target': config.get('Analysis', 'target_' + algo), 
					'prediction': config.get('Analysis', 'prediction_' + algo) }
