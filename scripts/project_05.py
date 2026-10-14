# Handwritten digits
# Public scikit-learn digits benchmark, 8x8 grayscale images; test against a majority-class baseline.
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import accuracy_score
X,y=load_digits(return_X_y=True)
a,b,c,d=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
for name,model in [('majority',DummyClassifier(strategy='most_frequent')),('kNN',KNeighborsClassifier(n_neighbors=3))]:
    model.fit(a,c)
    print(name,'accuracy:',round(accuracy_score(d,model.predict(b)),3))
print('Test digits:',len(d))
