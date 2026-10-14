import numpy as np
from sklearn.cluster import KMeans
X=np.array([[0,0],[0,1],[1,0],[8,8],[8,9],[9,8]], dtype=float)
km=KMeans(n_clusters=2,random_state=42,n_init=10).fit(X)
print('Cluster centers:',km.cluster_centers_.round(2).tolist())
print('Inertia:',round(km.inertia_,3))
print('Assignments:',km.labels_.tolist())
