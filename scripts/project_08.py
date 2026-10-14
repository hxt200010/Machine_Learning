# Anomaly detection
# Synthetic normal vibration readings with injected spikes; compare a statistical threshold with Isolation Forest.
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.metrics import precision_score,recall_score
rng=np.random.default_rng(7)
X=np.r_[rng.normal(0,1,150),rng.normal(6,.4,10)].reshape(-1,1)
y=np.r_[np.zeros(150,dtype=int),np.ones(10,dtype=int)]
threshold=(X[:,0]>3).astype(int)
forest=(IsolationForest(contamination=10/160,random_state=7).fit_predict(X)==-1).astype(int)
for name,pred in [('z-style threshold',threshold),('isolation forest',forest)]:
    print(name,'precision:',round(precision_score(y,pred,zero_division=0),3),
          'recall:',round(recall_score(y,pred,zero_division=0),3))
