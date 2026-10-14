import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([[1.],[2.],[3.],[4.]])
y = np.array([3.,5.,7.,9.])
model = LinearRegression().fit(x,y)
print('Slope:', round(float(model.coef_[0]), 4))
print('Intercept:', round(float(model.intercept_), 4))
print('Prediction for x=5:', round(float(model.predict([[5.]])[0]), 4))
