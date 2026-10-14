from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance
from sklearn.model_selection import train_test_split
X,y=load_breast_cancer(return_X_y=True)
a,b,c,d=train_test_split(X,y,random_state=7,stratify=y)
clf=RandomForestClassifier(n_estimators=40,random_state=7,n_jobs=1).fit(a,c)
result=permutation_importance(clf,b,d,n_repeats=3,random_state=7,n_jobs=1)
ix=result.importances_mean.argmax()
print('Test accuracy:',round(clf.score(b,d),3))
print('Most influential feature index:',int(ix))
print('Permutation accuracy drop:',round(result.importances_mean[ix],3))
