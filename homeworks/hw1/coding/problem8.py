# importing library
import numpy as np
import matplotlib.pyplot as plt
import random 


a = 0
b = 51 # need to include 50 so we add up 1
N = 500
zeroToFifty = np.random.uniform(a, b, 500) 
plt.plot(zeroToFifty)
plt.show()
plt.figure()
plt.hist(zeroToFifty, density = True, histtype = 'stepfilled', alpha = 0.2)
plt.show()
# print(zeroToFifty)

"""
a=1
b=100
N=100  
X1=np.random.uniform(a,b,N)
plt.plot(X1)
plt.show()
plt.figure()
plt.hist(X1, density=True, histtype='stepfilled', alpha=0.2)
#plt.show()
"""



"""
a=1
b=100
N=10000  
X2=np.random.uniform(a,b,N)

plt.figure()
plt.plot(X2)
plt.show()

plt.figure()
plt.hist(X2, density=True, histtype='stepfilled', alpha=0.2)
plt.show()

"""