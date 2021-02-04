import numpy as np
import matplotlib.pyplot as plt

N = 500 # N is the number of trials
n = 25 # n is the number of independent experiments in each trial
p = 0.1 # p is the probability of success for each experiment

P1 = np.random.binomial(n, p, N)
plt.plot(P1)
plt.figure()
plt.hist(P1, density = True, alpha = 0.8, histtype = 'bar', color = 'red', ec = 'black')
plt.show()

# Find probability of having 5 successes (that is p (X = 5))

res = []
for i, j in enumerate(P1):
	if j == 5:
	 res.append(i+1) # add the Xth = 5 in the new array

print(res)


