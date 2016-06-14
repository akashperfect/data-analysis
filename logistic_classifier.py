import numpy as np
import time, pickle

import graphlab, sys


# 	return personal_train

# def nearest_neighbour(train_data, label_str, feature_arr):

take_user_id = 'srch_destination_id'
take_item_id = 'hotel_cluster'


take_rows = sys.argv[1]
train_data = graphlab.SFrame.read_csv('train.csv', usecols=['user_id', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'srch_destination_id', 'srch_destination_type_id', 'hotel_continent', 'hotel_country', 'hotel_market', 'is_booking', 'hotel_cluster'], nrows=take_rows)
train_data = train_data[train_data['is_booking'] == 1]
train_1, test_1 = train_data.random_split(0.8, seed = 0)
# personal_train1 = similarity_recommender(train_1, 'user_id', 'hotel_cluster', 5)
# personal_train1 = graphlab.item_similarity_recommender.create(train_1, user_id=take_user_id, item_id=take_item_id, only_top_k=5)
# knn_model = graphlab.nearest_neighbors.create(train_1, features=['user_id', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'srch_destination_id', 'srch_destination_type_id', 'hotel_continent', 'hotel_country', 'hotel_market'])
logistic_model = graphlab.logistic_classifier.create(train_1, target='hotel_cluster', features=['user_id', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'srch_destination_id', 'srch_destination_type_id', 'hotel_continent', 'hotel_country', 'hotel_market'])

# print test_1
# prediction = knn.query(test_1)

# for row in prediction:
# print "abc"
# print test_1[0:1]
# print "next"
# print test_1[1:2]

# print train_1.num_rows()
# print prediction
targ_f = "target_lg.p"
pred_f = "prediction_lg.p"
temp = open(targ_f, "w")
temp.close()
temp = open(pred_f, "w")
temp.close()

# print train_1[10]
# print train_data[3]
# print train_data[14]
# print train_data[9]
target = [[]]
prediction =[[]]

counter = 0
num_items = 0

start = time.time()
global_start = time.time()
for i in range(1, test_1.num_rows() + 1):
    # print i
    curr_sframe = test_1[i-1:i]
    pred_model = logistic_model.predict_topk(curr_sframe, k=5).sort('probability', ascending=False)
    # print pred_model
    target.append([curr_sframe['hotel_cluster'].to_numpy().flatten()[0]])
    temp_list = []
    for model in pred_model:
        temp_list.append(model['class'])
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
pickle.dump(target[1:], open(targ_f,"ab"), -1)
pickle.dump(prediction[1:], open(pred_f,"ab"), -1)



print i
# print target[1:]
# print prediction[1:]

# for pred in prediction:
#     print train_1[pred['reference_label']]['hotel_cluster']

# print ""
# for row in train_1:
#     print row['user_id'], " ", row['hotel_cluster']

# print "test"
# for row in test_1:
#     print row['user_id'], " ", row['hotel_cluster']

# temp = open("targ_f.p", "w")
# temp.close()
# temp = open("pred_f.p", "w")
# temp.close()

# import numpy as np
# user1 = train_1[take_user_id].unique().to_numpy().flatten()
# user2_t = test_1[take_user_id].to_numpy().flatten()
# user2, user2_index = np.unique(user2_t, return_index=True)
# # inter = np.intersect1d(user1, user2, assume_unique=True)
# diff = np.setdiff1d(user2, user1, assume_unique=True)
# del(train_data)
# del(user1)
# del(train_1)
# print "Difference", diff.size
# print "Total Items =", user2_index.size
# cluster_id = dict()
# for x in diff:
# 	cluster_id[x] = 1
# target = [[]]
# prediction = [[]]
# start = time.time()
# print "Got Cluster"
# num_items = 0
# def get_predictions():
#     global user2_index, test_1, personal_train1, diff, target, prediction, num_items, start
#     counter = 0
#     for i in user2_index :
# 	    dest_id = int(test_1[i][take_user_id])
# 	    if (dest_id not in diff):
# 	    	counter += 1
# 	        target.append([test_1[i][take_item_id]])
# 	        curr_pred = (personal_train1.recommend(users=[dest_id])[take_item_id][0:5]).to_numpy().tolist()
# 	        prediction.append(curr_pred)
# 	        if(counter >= 1000):
# 	            pickle.dump(target, open("targ_f.p","ab"), -1)
# 	            pickle.dump(prediction, open("pred_f.p","ab"), -1)
# 	            target = [[]]
# 	            prediction = [[]]
# 	            num_items += counter
# 	            counter = 0
# 	            print float(num_items * 100.0) / float(user2_index.size), "Percentage Complete!" 
# 	            end = time.time()
# 	            print "time elapsed", end - start
# 	            start = end
#     pickle.dump(target, open("targ_f.p","ab"), -1)
#     pickle.dump(prediction, open("pred_f.p","ab"), -1)

# get_predictions()

# end = time.time()
# print("time taken", end - start)
# print num_items
print mapk(target[1:], prediction[1:], k=5)
# end = time.time()

# print("Map time taken", end - start)