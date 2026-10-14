# Recommendation baseline
# Toy user-item rating table with missing entries; compare popularity baseline with nearest-user weighted scoring.
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
R=np.array([[5,4,0,0],[4,5,1,0],[0,0,5,4],[0,1,4,5]],float)
observed=R>0
popularity=R.sum(0)/np.maximum(observed.sum(0),1)
user=0
similarity=cosine_similarity(R)[user].copy();similarity[user]=0
weighted=np.sum(similarity[:,None]*R,axis=0)/np.maximum(np.sum(similarity[:,None]*observed,axis=0),1e-9)
unseen=np.where(~observed[user])[0]
print('Unseen item indices:',unseen.tolist())
print('Popularity scores:',popularity[unseen].round(2).tolist())
print('Neighbor-weighted scores:',weighted[unseen].round(2).tolist())
