import numpy as np
import matplotlib.pyplot as plt

N = 500
n = 25
p = 0.1

P1 = np.random.binomial(n,p,N)


plt.figure()
plt.hist(P1, density=True, alpha=0.8, histtype='bar', color = 'green', ec='black')
plt.show()

