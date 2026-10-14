import numpy as np
from sklearn.ensemble import IsolationForest
X=np.array([0.,0.1,-0.2,0.2,-0.1,10.]).reshape(-1,1)
model=IsolationForest(contamination=1/6,random_state=42).fit(X)
print('Anomaly labels (-1 means outlier):',model.predict(X).tolist())
print('Anomaly values:',X[model.predict(X)==-1].ravel().tolist())
