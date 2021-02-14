import numpy as np
import matplotlib.pyplot as plt

# the sample sizes is 40
grades = np.array([55, 85, 72, 99, 48, 71, 88, 70, 59, 98, 80, 74, 93, 85, 74, 82, 90, 71, 83, 60, 95, 77, 84, 73, 63, 72, 95, 79, 51, 85, 76, 81, 78, 65, 75, 87, 86, 70, 80, 64])

"""
res = np.array([])
for i in range(len(grades)):
	res = np.append(res, grades[i])
	#print(type(res))
"""

# find the max sample: 99
# print(max(grades))
# find the min sample: 48
# print(min(grades))

# convert array grades to interval [0,1] 
grades = (grades - np.min(grades))/(np.max(grades) - np.min(grades))
print(grades)

# we will divide the samples into 20 parts so s = 20
# then count how many values of the sequence fall into each interval of amplitude 0.05.
# 0.05 = 1/ 20(parts)

# calculate the v variable
N = 40 # sample size
s = 20 # separate to 20 part
Ns = N/s
S = np.arange(0, 1, 0.05)
counts = np.empty(S.shape, dtype = int)
V = 0

for i in range(0, 20):
	counts[i] = len(np.where((grades >= S[i]) & (grades < S[i]+0.05))[0])
	V = V + (counts[i] - Ns)**2 / Ns

print("R = ",counts)
print("V = ", V)


Ypos = np.arange(len(counts))

plt.bar(Ypos,counts)
plt.show()

