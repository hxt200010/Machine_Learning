import numpy as np
from sklearn.linear_model import Ridge, Lasso
X = np.array([[1.,1.],[2.,1.],[3.,2.],[4.,3.],[5.,5.]])
y = np.array([2.,3.,5.,7.,9.])
for model in [Ridge(alpha=1.0), Lasso(alpha=0.1)]:
    model.fit(X,y)
    print(type(model).__name__, 'coefficients:', model.coef_.round(3).tolist())
