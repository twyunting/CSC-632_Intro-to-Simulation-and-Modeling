import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def probabilityDistribution(mu, sigma):
	Y = np.random.normal(mu, sigma)
	PlotY = sns.distplot(Y)
	plt.figure()
	plt.show()
	plt.hist(zeroToFifty, density = True, histtype = 'stepfilled', alpha = 0.5)
	# Display all open figures
	plt.show()



probabilityDistribution(25, 3)
probabilityDistribution(25, 4)
probabilityDistribution(25, 5)
