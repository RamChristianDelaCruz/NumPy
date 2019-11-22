import numpy as np
X = np.random.random((5,5))*100
XNot = np.average(X)
Sigma = np.std(X)
Z = (X - XNot)/(Sigma)
np.save('X_normalization.npy', Z)