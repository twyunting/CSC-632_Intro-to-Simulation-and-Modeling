import numpy as np
import math
import random
import matplotlib.pyplot as plt

random.seed(2)
f = lambda x:2*x/(2-x) # using syntax without define a new function 
a = 0.0
b = 5.0
NumSteps = 1000000
XIntegral=[]  
YIntegral=[]
XRectangle=[]  
YRectangle=[]

ymin = f(a)
ymax = ymin
# extract min and max in the distribution
for i in range(NumSteps):
    x = a + (b - a) * float(i) / NumSteps # calculate the rectangle area
    y = f(x)
    if y < ymin: 
      ymin = y
    if y > ymax: 
      ymax = y

# applying in Monte Carlo method
A = (b - a) * (ymax - ymin)
N = 1000000 # set the numbers of random pairs we want to generate
M = 0 # the number of points that fall under the curve that represents f(x)
for k in range(N):
    x = a + (b - a) * random.random()
    y = ymin + (ymax - ymin) * random.random()
    if y <= f(x):
            M += 1 
            XIntegral.append(x)
            YIntegral.append(y)  
    else:
            XRectangle.append(x) 
            YRectangle.append(y)              
NumericalIntegral = M / N * A
print ("Numerical integration = " + str(NumericalIntegral))

XLin=np.linspace(a,b)
YLin=[]
for x in XLin:
    YLin.append(f(x))

plt.axis   ([0, b, 0, f(b)])                                            
plt.plot   (XLin,YLin, color="red" , linewidth="4") 
plt.scatter(XIntegral, YIntegral, color="blue", marker  =".") 
plt.scatter(XRectangle, YRectangle, color="yellow", marker   =".")
plt.title  ("Numerical Integration using Monte Carlo method")
plt.show()
