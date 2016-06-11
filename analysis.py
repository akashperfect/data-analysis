import numpy as np 
import pickle

from getConfig import conf

targ_f = conf['target_filename']
pred_f = conf['prediction_filename']
mapping_k = conf['mapk']
path = conf['path']
target = [[]]
prediction = [[]]
with open(targ_f, "rb") as f:
    try:
        while True:
            ind = pickle.load(f)
            for l in ind:
                if l != []:
                    target.append(l)
    except EOFError:
        pass

with open(pred_f, "rb") as f:
    try:
        while True:
            ind = pickle.load(f)
            for l in ind:
                if len(l) != 0:
                    prediction.append(l)
    except EOFError:
        pass


def apk(actual, predicted, k=10):
    if len(predicted)>k:
        predicted = predicted[:k]

    score = 0.0
    num_hits = 0.0
    for i,p in enumerate(predicted):
        if p in actual and p not in predicted[:i]:
            num_hits += 1.0
            score += num_hits / (i+1.0)

    if not actual:
        return 0.0

    return score / min(len(actual), k)

def mapk(actual, predicted, k=10):
    return np.mean([apk(a,p,k) for a,p in zip(actual, predicted)])


print "Length of Target", len(target)
print "Length of Prediction", len(prediction)

print "First 100 values target & prediction"
for i in range(0, 100):
    print target[i], prediction[i]

print mapk(target, prediction, k=mapping_k)

