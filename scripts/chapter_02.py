import numpy as np
import pandas as pd
features = np.array([[1., 2.], [2., 3.], [3., 4.]])
weights = np.array([0.6, 0.4])
scores = features @ weights
frame = pd.DataFrame(features, columns=['feature_a', 'feature_b'])
frame['score'] = scores
print(frame.to_string(index=False))
print('Mean score:', round(float(scores.mean()), 3))
