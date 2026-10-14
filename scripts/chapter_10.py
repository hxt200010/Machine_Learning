import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
X = np.array([['10','red'],['20','blue'],['30','red'],['40','blue']])
y = np.array([0,0,1,1])
pre = ColumnTransformer([('num', StandardScaler(), [0]),
 ('cat', OneHotEncoder(handle_unknown='ignore'), [1])])
pipe = Pipeline([('preprocess', pre), ('model', LogisticRegression())]).fit(X,y)
print('Predictions:', pipe.predict(X).tolist())
print('Transformed feature count:', pipe.named_steps['preprocess'].transform(X).shape[1])
