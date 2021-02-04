import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mu = 25
sigma = 3
Y = np.random.normal(mu, sigma)
PlotY = sns.distplot(Y)
plt.figure()
plt.show()
print(Y)