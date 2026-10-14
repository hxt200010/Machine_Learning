# Customer segmentation
# Synthetic three-group purchasing profiles; compare k-means against a one-centroid baseline via inertia.
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
X,_=make_blobs(n_samples=240,centers=[[5,10],[30,50],[60,20]],cluster_std=4,random_state=42)
Z=StandardScaler().fit_transform(X)
for k in [1,3]:
    model=KMeans(n_clusters=k,random_state=42,n_init=10).fit(Z)
    print('Clusters:',k,'inertia:',round(model.inertia_,2))
print('Synthetic customers:',len(X))
