import numpy as np
import math

# the sample sizes is 40
grades = np.array([55, 85, 72, 99, 48, 71, 88, 70, 59, 98, 80, 74, 93, 85, 74, 82, 90, 71, 83, 60, 95, 77, 84, 73, 63, 72, 95, 79, 51, 85, 76, 81, 78, 65, 75, 87, 86, 70, 80, 64])
#print(len(grades))
res=[]
for i in grades:
	tmp = np.array([i])
	res.append(tmp)
#print(res)
# testing for 40 arrays	
#for i in res:
	#print(i)


# find the max sample: 99
# print(max(grades))
# find the min sample: 48
# print(min(grades))

# we will divide the samples into 20 parts
s = 20
# then count how many values of the sequence fall into each interval of amplitude 0.05.
# 0.05 = 1/ 20(parts)


# calculate the v variable
N = 40 # sample size
s = 20 # separate to 20 part
Ns = N/s
S = np.arange(48, 99, 0.05)
counts = np.empty(S.shape, dtype = int)
V = 0

for i in range(20):
	counts[i] = len(np.where((grades >= S[i]) & (grades < S[i]+0.05))[0])
	V = V + (counts[i] - Ns)**2 / Ns

print("R = ",counts)
print("V = ", V)


