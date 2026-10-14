# Chronological time-series forecasting
# Synthetic trend-plus-seasonality series, lag-based forecasting vs naive last-value baseline.
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
rng=np.random.default_rng(7);t=np.arange(140)
y=10+.06*t+2*np.sin(2*np.pi*t/12)+rng.normal(0,.4,len(t))
X=np.column_stack([y[:-2],y[1:-1]]);target=y[2:]
cut=110;model=LinearRegression().fit(X[:cut],target[:cut])
pred=model.predict(X[cut:]);naive=X[cut:,1]
print('Chronological holdout points:',len(pred))
print('Last-value MAE:',round(mean_absolute_error(target[cut:],naive),3))
print('Linear lag model MAE:',round(mean_absolute_error(target[cut:],pred),3))
