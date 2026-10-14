import numpy as np
from scipy.stats import t
x = np.array([4, 7, 5, 6, 8, 5, 7], dtype=float)
se = x.std(ddof=1)/np.sqrt(len(x))
margin = t.ppf(0.975, df=len(x)-1)*se
print('Sample mean:', round(x.mean(), 3))
print('95% CI:', tuple(round(z, 3) for z in (x.mean()-margin, x.mean()+margin)))
print('Interpretation: repeated intervals cover true means ~95% in the long run.')
