import numpy as np
import matplotlib.pyplot as plt

N = 500 # N is the number of trials
n = 25 # n is the number of independent experiments in each trial
p = 0.1 # p is the probability of success for each experiment

P1 = np.random.binomial(n, p, N)
plt.plot(P1)

plt.figure()
plt.hist(P1, density=True, alpha=0.8, histtype='bar', color = 'green', ec='black')
plt.show()

# Find probability of having 5 successes (that is p (X = 5))

count = 0
for i in range(len(P1)):
	if P1[i] == 5:
		count += 1


print(count/500)


