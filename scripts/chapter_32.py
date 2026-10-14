from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
X,y=load_digits(return_X_y=True)
a,b,c,d=train_test_split(X,y,test_size=0.2,random_state=7,stratify=y)
model=KNeighborsClassifier(n_neighbors=3).fit(a,c)
print('Image size in pixels:',X.shape[1])
print('Test accuracy:',round(model.score(b,d),3))
print('Classes:',len(set(y)))
