from sklearn.datasets import make_moons
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
X,y = make_moons(n_samples=300, noise=0.15, random_state=7)
Xtr,Xte,ytr,yte = train_test_split(X,y,random_state=7)
for kernel in ['linear','rbf']:
    clf=SVC(kernel=kernel,gamma='scale').fit(Xtr,ytr)
    print(kernel, 'test accuracy:', round(clf.score(Xte,yte),3), 'support vectors:',len(clf.support_))
