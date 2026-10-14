from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
X,y=load_wine(return_X_y=True)
a,b,c,d=train_test_split(X,y,random_state=7,stratify=y)
for clf in [RandomForestClassifier(n_estimators=50,random_state=7),GradientBoostingClassifier(random_state=7)]:
    clf.fit(a,c)
    print(type(clf).__name__, 'test accuracy:', round(clf.score(b,d),3))
