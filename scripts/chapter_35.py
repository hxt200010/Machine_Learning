# Bayesian coin learning with Beta prior and Bernoulli outcomes.
from scipy.stats import beta
alpha_prior,beta_prior=2,2
successes,failures=8,2
a=alpha_prior+successes
b=beta_prior+failures
print('Posterior Beta parameters:',(a,b))
print('Posterior mean:',round(a/(a+b),3))
print('95% credible interval:',tuple(round(v,3) for v in beta.ppf([0.025,0.975],a,b)))
