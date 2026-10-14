import numpy as np
import pandas as pd
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 8, 11], dtype=float)
df = pd.DataFrame({'x': x, 'y': y})
print('Feature means:', df.mean().round(2).to_dict())
print('Pearson correlation:', round(df.corr().loc['x','y'], 3))
print('Caution: correlation alone does not establish causation.')
