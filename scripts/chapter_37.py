from pathlib import Path
import joblib
from sklearn.datasets import load_iris
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
X,y=load_iris(return_X_y=True)
model=make_pipeline(StandardScaler(),LogisticRegression(max_iter=300)).fit(X,y)
path=Path(__file__).with_suffix('.joblib')
joblib.dump(model,path)
loaded=joblib.load(path)
print('Serialized model bytes:',path.stat().st_size)
print('Prediction matches:',bool((model.predict(X[:5])==loaded.predict(X[:5])).all()))
path.unlink()
