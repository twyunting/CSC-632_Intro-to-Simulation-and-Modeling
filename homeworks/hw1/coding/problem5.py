import random

# a) Generate 20 Pseudorandom numbers between 0 and 1.
"""
for i in range(20):
	print('%05.4f' % random.random(), end=" ")
print()


# b) Do part (a) using random.seed() function to generate the same list of random variables.
random.seed(69) # set as the same random numbers

for i in range(20):

    print('%05.4f' % random.random(), end=' ')

print()


# c) Make a random number generator using a “for-loop” that generates integer random numbers 'n' number of times

def randomNumberGenerator(n):
	for i in range(n):
		print(random.random()) # The random() method returns a random floating number between 0 and 1.

randomNumberGenerator(10)
"""

# d) Use a random generator to select three “same” sets of random countries from the following list.
countriesList = [Canada, USA, Italy, China, India, South Africa, Spain, Brazil, Mexico]
for i in range(10):
    countriesItem = random.choice(countriesList)
    print ("Randomly selected item from Cities list is - ", countriesItem)



