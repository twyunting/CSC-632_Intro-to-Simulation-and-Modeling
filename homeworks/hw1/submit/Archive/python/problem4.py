import numpy as np

# 4a Linear congruential generator 
a, c, m, x = 3, 4, 5, 3

for i in range(100): # run 100 times
	x = np.mod((a*x+c), m) # Return element-wise remainder of division
	print(x) # Because a*x+ =13 and the remainder of division 5 is 3 



# 4b Learmonth-Lewis generator

a = 60
c = 0
m = 2**(31) -1
x = 0.1

for i in range(100):

    x= np.mod((a*x+c),m)

    uniform = x/m # generation of a uniform distribution in the range of [0, 1]

    print(uniform)


# 4c Lagged Fibonacci generator
x0 = x1 = 1
m = 2**32


for i in range(100):
	x = np.mod((x0+x1), m)
	x0 = x1
	x1 = x
	print(x)


