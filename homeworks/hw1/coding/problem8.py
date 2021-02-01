# importing library
import numpy as np
import matplotlib.pyplot as plt
import random 

a = 0
b = 51 # needs to include 50 so we add up 1
n = 50

# create a function
def zeroToFifty(a, b, n):
	zeroToFifty = np.random.uniform(a, b, n)
	# stepfilled' generates a lineplot that is by default filled
	# density = True: draw and return a probability density:
	plt.hist(zeroToFifty, density = True, histtype = 'stepfilled', alpha = 0.5)
	# Display all open figures
	plt.show()

# Using for loop to repeat the same graph by replicating 500 samples 
for i in range(500):
	zeroToFifty(a, b, n)
