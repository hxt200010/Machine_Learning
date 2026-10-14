import numpy as np
from sklearn.decomposition import PCA
X=np.array([[1,1],[2,2],[3,3],[4,4]],dtype=float)
pca=PCA(n_components=1).fit(X)
print('Explained variance ratio:',pca.explained_variance_ratio_.round(4).tolist())
print('First direction:',np.abs(pca.components_[0]).round(4).tolist())
print('Reduced shape:',pca.transform(X).shape)
