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
test_data_full.save(test_sf)

if()
print ''
print "Column Names"
columnNumber = 0
columnArray = []
for i in train_data_full.column_names():
    print "[" + str(columnNumber) + "] " + i
    columnNumber += 1
    columnArray.append(i)

features_used = raw_input("Choose feature(s) separated by comma to be used in KNN Model (default: all): ")
target = input("Choose target variable which needs to be predicted: ")
filtering = raw_input("If any filtering to be applied input the column number")




