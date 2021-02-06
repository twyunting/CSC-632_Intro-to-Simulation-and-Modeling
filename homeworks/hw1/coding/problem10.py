import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# add 1000
def probabilityDistribution(mu, sigma):
	Y = np.random.normal(mu, sigma, 1000)
	PlotY = sns.distplot(Y)
	plt.show()
	plt.figure()
	plt.hist(Y, density = True, histtype = 'stepfilled', alpha = 0.5, color = "green", ec = 'black')
	plt.show()
	
	# FindP (Y>20)
	greaterThanTwenty = []
	for i, j in enumerate(Y):
		if j > 20:
	 		greaterThanTwenty.append(i+1) # add the Yth > 20 in the new array

	print(len(greaterThanTwenty)/1000)

	# Find P (Y = 22.5)
	equalTewntyFivePointFive = []
	for k, l in enumerate(Y):
		if l == 22.5:
	 		equalTewntyFivePointFive.append(k+1) # add the Yth == 22.5 in the new array
	print(len(equalTewntyFivePointFive)/1000)


probabilityDistribution(25, 3)
probabilityDistribution(25, 4)
probabilityDistribution(25, 5)


