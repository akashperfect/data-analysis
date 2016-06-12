import graphlab
from getConfig import conf

train_data = conf['train_data']
test_data = conf['test_data']
train_sf = conf['train_data_sf']
test_sf = conf['test_data_sf']
path = conf['path']
title = conf['title']

train_data_full = graphlab.SFrame.read_csv(train_data)
test_data_full = graphlab.SFrame.read_csv(test_data)

train_data_full.save(train_sf)
test_data_full.save(test_data)
