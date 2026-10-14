import numpy as np
rng = np.random.default_rng(42)
flips = rng.binomial(n=1, p=0.30, size=10000)
print('Analytical mean:', 0.30)
print('Empirical mean:', round(float(flips.mean()), 4))
print('Analytical variance:', round(0.3*0.7, 4))
print('Estimated variance:', round(float(flips.var()), 4))
