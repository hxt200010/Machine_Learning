from sklearn.datasets import load_iris
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
X,y=load_iris(return_X_y=True)
pipe=make_pipeline(StandardScaler(),SVC())
search=GridSearchCV(pipe,{'svc__C':[0.1,1,10],'svc__kernel':['linear','rbf']},cv=5)
search.fit(X,y)
print('Best settings:',search.best_params_)
print('Mean CV accuracy:',round(search.best_score_,3))
