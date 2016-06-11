import numpy as np
import time, pickle

import graphlab, sys



take_user_id = 'srch_destination_id'
take_item_id = 'hotel_cluster'

train_data = graphlab.SFrame.read_csv('train.csv', usecols=['user_id', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'srch_destination_id', 'srch_destination_type_id', 'hotel_continent', 'hotel_country', 'hotel_market', 'is_booking', 'hotel_cluster'])
train_data = train_data[train_data['is_booking'] == 1]
train_1, test_1 = train_data.random_split(0.8, seed = 0)
knn_model = graphlab.nearest_neighbors.create(train_1, features=['user_id', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'srch_destination_id', 'srch_destination_type_id', 'hotel_continent', 'hotel_country', 'hotel_market'])



targ_f = "target_knn.p"
pred_f = "prediction_knn.p"
temp = open(targ_f, "w")
temp.close()
temp = open(pred_f, "w")
temp.close()

target = [[]]
prediction =[[]]

counter = 0
num_items = 0

start = time.time()
global_start = time.time()

print "test rows", test_1.num_rows()

steps = 50000
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
        target.append([curr_sframe[i - row]['hotel_cluster']])
        temp_list = []
        for model in range(i * 5, (i + 1) * 5) :
            temp_list.append(train_1[pred_model[model]['reference_label']]['hotel_cluster'])
        prediction.append(temp_list)
        counter += 1
        if(counter >= 2000):
            pickle.dump(target[1:], open(targ_f,"ab"), -1)
            pickle.dump(prediction[1:], open(pred_f,"ab"), -1)
            target = [[]]
            prediction = [[]]
            num_items += counter
            counter = 0
            print float(num_items * 100.0) / float(test_1.num_rows()), "Percentage Complete!" 
            end = time.time()
            print num_items, "records done"
            print "time elapsed", end - start
            print "total time", end - global_start
            print ''
            start = end
    row += limit
    pickle.dump(target[1:], open(targ_f,"ab"), -1)
    pickle.dump(prediction[1:], open(pred_f,"ab"), -1)


print "total rows ", test_1.num_rows()
print "items", num_items
