import numpy as np
from sklearn.linear_model import LinearRegression
series=np.array([10,12,14,15,18,20,21,24],dtype=float)
X=np.column_stack([series[:-2],series[1:-1]])
y=series[2:]
model=LinearRegression().fit(X,y)
print('Lag-window shape:',X.shape)
print('Next forecast:',round(float(model.predict([[21,24]])[0]),3))
print('Caution: chronological testing is essential for genuine evaluation.')
