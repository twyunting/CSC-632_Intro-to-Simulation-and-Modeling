# import libraries
import numpy as np
import matplotlib.pyplot as plt
import random 

a = 1
b = 50 # needs to include 50 so we add up 1
n = 50

# create a function
def zeroToFifty(a, b, n):
	zeroToFifty = np.random.uniform(a, b, n)
	# Draw a diagram with 50 random numbers
	plt.plot(zeroToFifty)
	plt.show()
	plt.figure() # The purpose of using plt.figure() is to create a figure object.
	# stepfilled' generates a lineplot that is by default filled
	# density = True: draw and return a probability density:
	plt.hist(zeroToFifty, density = True, histtype = 'stepfilled', alpha = 0.5)
	# Display all open figures
	plt.show()
	
zeroToFifty(a, b, n)

# Using for loop to repeat the same graph by replicating 500 samples 
n = 500
zeroToFifty(a, b, n)

