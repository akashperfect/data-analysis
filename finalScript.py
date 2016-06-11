import graphlab, sys
import numpy as np
import time, pickle

# def similarity_recommender(train_data, user_id_para, item_id, top_rows):
# 	return personal_train

# def nearest_neighbour(train_data, label_str, feature_arr):


# take_rows = sys.argv[1]
train_data = graphlab.SFrame.read_csv('train.csv', usecols=['user_id', 'is_booking', 'hotel_cluster'])
test_data = graphlab.SFrame.read_csv('test.csv', usecols=['id', 'user_id'])
train_data = train_data[train_data['is_booking'] == 1]
# personal_train1 = similarity_recommender(train_1, 'user_id', 'hotel_cluster', 5)
personal_train1 = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='hotel_cluster', only_top_k=5)
# knn = graphlab.nearest_neighbors.create(people, features=['hotel_cluster', 'srch_adults_cnt', 'srch_children_cnt', 'srch_rm_cnt', 'srch_destination_id', 'srch_destination_type_id', 'hotel_continent', 'hotel_country', 'hotel_market', 'cnt'], label='user_id')

# temp = open("target_f_later.p", "w")
# temp.close()
# temp = open("prediction_f_later.p", "w")
# temp.close()

import numpy as np
target = [[]]
prediction = [[]]
start = time.time()
print "Got Cluster"
num_items = 0
counter = 0
target = [[]]
prediction = [[]]

for row in range(1706001, test_data.num_rows()) :
    user_id = int(test_data[row]['user_id'])
    counter += 1
    target.append(int(test_data[row]['id']) )
    curr_pred = (personal_train1.recommend(users=[user_id])['hotel_cluster'][0:5]).to_numpy().tolist()
    prediction.append(curr_pred)
    if(counter >= 1000):
        pickle.dump(target, open("target_f.p","ab"), -1)
        pickle.dump(prediction, open("prediction_f.p","ab"), -1)
        target = [[]]
        prediction = [[]]
        num_items += counter
        counter = 0
        print float(num_items * 100.0) / float(test_data.num_rows()), "Percentage Complete!" 
        end = time.time()
        print "time elapsed", end - start
        start = end
pickle.dump(target, open("target_f.p","ab"), -1)
pickle.dump(prediction, open("prediction_f.p","ab"), -1)

get_predictions()

end = time.time()
print("time taken", end - start)
print num_items
# print mapk(target, prediction, k=5)
# end = time.time()

# print("Map time taken", end - start)