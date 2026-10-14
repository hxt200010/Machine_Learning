import numpy as np
A = np.array([[3., 1.], [1., 3.]])
values, vectors = np.linalg.eigh(A)
U, s, Vt = np.linalg.svd(A)
print('Eigenvalues:', values.round(3))
print('Singular values:', s.round(3))
print('Reconstruction error:', round(float(np.linalg.norm(U @ np.diag(s) @ Vt-A)), 9))
