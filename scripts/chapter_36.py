from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error
X,y=load_diabetes(return_X_y=True)
a,b,c,d=train_test_split(X,y,random_state=42,test_size=0.2)
model=make_pipeline(StandardScaler(),Ridge(alpha=10)).fit(a,c)
print('Training rows:',len(c),'test rows:',len(d))
print('Holdout MAE:',round(mean_absolute_error(d,model.predict(b)),2))
