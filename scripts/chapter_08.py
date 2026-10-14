import numpy as np
import pandas as pd
df = pd.DataFrame({'temperature':[20., np.nan, 24., 22.], 'fault':[0,0,1,0]})
print('Missing values:', df.isna().sum().to_dict())
print('Median temperature:', df.temperature.median())
print('Class counts:', df.fault.value_counts().sort_index().to_dict())
