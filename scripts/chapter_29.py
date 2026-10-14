import numpy as np
rng=np.random.default_rng(7)
latent=rng.normal(size=(5,2))
W=np.array([[1.5,0.2],[-0.1,2.0]])
samples=latent@W.T
print('Generated sample shape:',samples.shape)
print('Mean of five synthetic samples:',samples.mean(axis=0).round(3).tolist())
print('Note: this is a toy latent-variable generator, not a trained GAN or VAE.')
