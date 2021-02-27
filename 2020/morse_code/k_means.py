import random
import math

DATA_SHORT = [1, 1.1, 1.3, 1.4, 0.8, 0.9, 1, 1.1, 0.9, 0.8, 1.1, 1.2, 1.3, 0.7]
DATA_LONG = [5, 4.8, 5.3, 5.6, 5, 4.9, 5.1, 5.2, 5.3, 5.2, 5.0, 5.3, 5.2, 4.8, 4.5]

ALL_DATA = DATA_SHORT + DATA_LONG

def FindMinMax(items):
	return min(items), max(items)

def InitializeMeans(k, cMin, cMax):
	return [random.uniform(cMin+1, cMax-1) for i in range(k)]

def EuclideanDistance(x, y):
	return math.sqrt(math.pow(x-y, 2))

def UpdateMean(n, mean, item):
	return round((mean*(n-1)+item)/float(n) , 3)

def Classify(means, item):
	return 0 if EuclideanDistance(item, means[0]) < EuclideanDistance(item, means[1]) else 1

def CalculateMeans(k, items, maxIterations=100000):
	cMin, cMax = FindMinMax(items)

	means = InitializeMeans(k, cMin, cMax)

	clusterSizes = [0] * len(means)
	belongsTo = [0] * len(items)

	for e in range(maxIterations):

		noChange = True 
		for i in range(len(items)):

			item = items[i]

			index = Classify(means, item)

			clusterSizes[index] += 1
			cSize = clusterSizes[index]
			means[index] = UpdateMean(cSize, means[index], item)

			if(index != belongsTo[i]):
				noChange = False 

			belongsTo[i] = index

		if (noChange):
			break

	return means

print(CalculateMeans(2, ALL_DATA))
