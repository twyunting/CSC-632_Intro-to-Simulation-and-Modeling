import numpy as np

a = 75

c = 0

m = 2**(31) -1

x = 0.1

u=np.array([])

for i in range(0,100):

    x= np.mod((a*x+c),m)

    u= np.append(u,x/m)

    print(len(u))