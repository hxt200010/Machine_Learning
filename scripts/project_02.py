# Diabetes-outcome regression
# scikit-learn load_diabetes benchmark (real standardized features; quantitative disease-progression target, not a diagnostic class).
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_absolute_error
X,y=load_diabetes(return_X_y=True)
a,b,c,d=train_test_split(X,y,test_size=.2,random_state=42)
models={'mean baseline':DummyRegressor(strategy='mean'),
        'ridge':make_pipeline(StandardScaler(),Ridge(alpha=10.0))}
for name,model in models.items():
    model.fit(a,c)
    print(name,'MAE:',round(mean_absolute_error(d,model.predict(b)),2))
print('Test set size:',len(d))
