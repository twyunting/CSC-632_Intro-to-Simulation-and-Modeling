import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# add 1000
def probabilityDistribution(mu, sigma):
	Y = np.random.normal(mu, sigma, 1000)
	PlotY = sns.distplot(Y)
	plt.show()
	#plt.figure()
	#plt.hist(zeroToFifty, density = True, histtype = 'stepfilled', alpha = 0.5)
	# Display all open figures
	



probabilityDistribution(25, 3)
probabilityDistribution(25, 4)
probabilityDistribution(25, 5)
