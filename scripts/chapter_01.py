# Supervised learning predicts known labels; clustering discovers groups.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score
X, y = load_iris(return_X_y=True)
Xtr, Xte, ytr, yte = train_test_split(X, y, stratify=y, random_state=7)
clf = LogisticRegression(max_iter=1000).fit(Xtr, ytr)
cluster = KMeans(n_clusters=3, n_init=10, random_state=7).fit(X)
print('Labeled examples:', len(y))
print('Test accuracy:', round(accuracy_score(yte, clf.predict(Xte)), 3))
print('Cluster sizes:', sorted(__import__('numpy').bincount(cluster.labels_)))
