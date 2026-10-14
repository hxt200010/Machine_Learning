# House-price baseline
# Synthetic square-footage data; baseline is predicting training mean. Demonstrates regression split and MAE.
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
rng=np.random.default_rng(11)
area=rng.uniform(800,3200,250).reshape(-1,1)
price=60000+210*area[:,0]+rng.normal(0,35000,250)
Xtr,Xte,ytr,yte=train_test_split(area,price,test_size=.2,random_state=42)
model=LinearRegression().fit(Xtr,ytr)
naive=np.full_like(yte,ytr.mean())
print('Dataset: 250 synthetic properties')
print('Mean baseline MAE:',round(mean_absolute_error(yte,naive)))
print('Linear regression MAE:',round(mean_absolute_error(yte,model.predict(Xte))))
print('Fitted USD/sq ft:',round(model.coef_[0],2))
