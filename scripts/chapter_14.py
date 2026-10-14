import numpy as np
from sklearn.linear_model import LogisticRegression
X = np.array([[0.],[1.],[2.],[3.],[4.],[5.]])
y = np.array([0,0,0,1,1,1])
model = LogisticRegression().fit(X,y)
print('Class probabilities at x=2.5:', model.predict_proba([[2.5]]).round(3).tolist())
print('Prediction at x=4:', model.predict([[4]]).tolist())
