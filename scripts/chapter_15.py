import numpy as np
from sklearn.neighbors import KNeighborsClassifier
X = np.array([[0,0],[1,0],[0,1],[4,4],[5,4],[4,5]])
y = np.array([0,0,0,1,1,1])
model = KNeighborsClassifier(n_neighbors=3).fit(X,y)
print('Neighbor distances:',np.linalg.norm(X-[0.5,0.5],axis=1).round(3).tolist())
print('Predicted class:', model.predict([[0.5,0.5]]).tolist())
