import numpy as np
from sklearn.metrics import precision_score, recall_score
truth = np.array([0,0,0,1,1,1])
prob = np.array([0.1,0.4,0.55,0.45,0.75,0.9])
for threshold in [0.5,0.7]:
    pred = (prob >= threshold).astype(int)
    print('Threshold', threshold, 'precision',round(precision_score(truth,pred),3),
          'recall',round(recall_score(truth,pred),3))
