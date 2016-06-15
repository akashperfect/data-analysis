import numpy as np
from getConfig import conf
import time, pickle, datetime, os

import graphlab, sys

train_sf = conf['train_data_sf']
test_sf = conf['test_data_sf']
path = conf['path']
title = conf['title']
targ_file = conf['KNN']['target']
pred_file = conf['KNN']['prediction']
knn_model_file = conf['KNN']['model']
steps = int(conf['KNN']['steps'])
file_max_records = int(conf['KNN']['file_max_records'])

target = [[]]
prediction =[[]]

counter = 0
num_items = 0

train_data = graphlab.load_sframe(train_sf).sample(0.005, seed=0)
train_1, test_1 = train_data.random_split(0.8, seed = 0)

columnArray = train_data.column_names()

if(os.path.exists(knn_model_file) == False):

    print ''
    print "Column Names"
    columnNumber = 0
    for i in columnArray:
        print "[" + str(columnNumber) + "] " + i
        columnNumber += 1

    features_used = raw_input("Choose feature(s) separated by comma to be used in KNN Model (default: all): ")
    target = input("Choose target variable which needs to be predicted: ")
    filtering = raw_input("If any filtering to be applied input the column number")

    target_var = columnArray[target]


    if(filtering != ""):
        train_data = train_data[train_data[columnArray[int(filtering)]] == 1]

    features_applied = []
    for ids in features_used.split(','): 
        features_applied.append(columnArray[int(ids)])

    print "Features To Be Used"
    print features_applied

    knn_model = graphlab.nearest_neighbors.create(train_1, features=features_applied)

    knn_model.save(knn_model_file)

else:
    knn_model = graphlab.load_model(knn_model_file)

## Initializing files 
temp = open(targ_file, "w")
temp.close()
temp = open(pred_file, "w")
temp.close()

columnArray

target_var = columnArray[len(columnArray) - 1]

print "Target", target_var

start = time.time()
global_start = time.time()

print "Number of Test Rows", test_1.num_rows()

row = 0
while (row < test_1.num_rows()):
    limit = steps
    if(row + steps > test_1.num_rows()):
        limit = test_1.num_rows()
    curr_sframe = test_1[row:limit]
    pred_model = knn_model.query(curr_sframe, verbose=False)
    print "row", row
    print "limit", limit
    for i in range(row, limit):
        target.append([curr_sframe[i - row][target_var]])
        temp_list = []
        for model in range(i * 5, (i + 1) * 5) :
            temp_list.append(train_1[pred_model[model]['reference_label']][target_var])
        prediction.append(temp_list)
        counter += 1
        if(counter >= file_max_records):
            pickle.dump(target[1:], open(targ_file,"ab"), -1)
            pickle.dump(prediction[1:], open(pred_file,"ab"), -1)
            target = [[]]
            prediction = [[]]
            num_items += counter
            counter = 0
            end = time.time()
            print float(num_items * 100.0) / float(test_1.num_rows()), "Percentage Complete!" 
            print num_items, "records done"
            print "time elapsed", end - start
            print "total time", end - global_start
            print "Current Time", str(datetime.datetime.now().time())
            print ''
            start = end
    row += limit
    pickle.dump(target[1:], open(targ_file,"ab"), -1)
    pickle.dump(prediction[1:], open(pred_file,"ab"), -1)


print "total rows ", test_1.num_rows()
print "items", num_items
