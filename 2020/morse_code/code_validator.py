import random
import math
import time

DATA_SHORT = [1, 1.1, 1.3, 1.4, 0.8, 0.9, 1, 1.1, 0.9, 0.8, 1.1, 1.2, 1.3, 0.7]
DATA_LONG = [5, 4.8, 5.3, 5.6, 5, 4.9, 5.1, 5.2, 5.3, 5.2, 5.0, 5.3, 5.2, 4.8, 4.5]

ALL_DATA = DATA_SHORT + DATA_LONG

#########################
### MORSE CODE LOOKUP ###
#########################

MORSE_CODE = {
	"A": [".", "-"],
	"B": ["-", ".", ".", "."],
	"C": ["-", ".", "-", "."],
	"D": ["-", ".", "."],
	"E": ["."],
	"F": [".", ".", "-", "."],
	"G": ["-", "-", "."],
	"H": [".", ".", ".", "."],
	"I": [".", "."],
	"J": [".", "-", "-", "-"],
	"K": ["-", ".", "-"],
	"L": [".", "-", ".", "."],
	"M": ["-", "-"],
	"N": ["-", "."],
	"O": ["-", "-", "-"],
	"P": [".", "-", "-", "."],
	"Q": ["-", "-", ".", "-"],
	"R": [".", "-", "."],
	"S": [".", ".", "."],
	"T": ["-"],
	"U": [".", ".", "-"],
	"V": [".", ".", ".", "-"],
	"W": [".", "-", "-"],
	"X": ["-", ".", ".", "-"],
	"Y": ["-", ".", "-", "-"],
	"Z": ["-", "-", ".", "."]
}

#########################
### K-MEANS ALGORITHM ###
#########################

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

#######################
### DATA COLLECTION ###
#######################

def GetDataArray(tsensor):
	data = []
	down = False
	start = None
	while True:
		if Button.Center in brick.buttons():
			return data
		if tsensor.pressed():
			if not down:
				down = True
				start = time.time()
		else:
			if down:
				data.append(time.time() - start)
				down = False

########################
### LOOKUP FUNCTION ####
########################

def findLetter(letter, dot, dash):
	translation = []
	for item in letter:
		dis1 = EuclideanDistance(item, dot)
		dis2 = EuclideanDistance(item, dash)
		translation.append("." if dis1 < dis2 else "-")
	for key in MORSE_CODE:
		if translation == MORSE_CODE[key]:
			return key
	return None

########################
### DISPLAY FUNCTION ###
########################

def display(message):
	brick.display.text(message)

#####################
### MAIN FUNCTION ###
#####################

def main():

	clusters = CalculateMeans(2, ALL_DATA)

	dot = min(clusters)
	dash = max(clusters)

	A = [1.2, 5.3]
	I = [1.2, 0.8]
	T = [5.4]
	Y = [5, 0.7, 4.8, 5.5]

	print("A evaluates to {}".format(findLetter(A, dot, dash)))
	print("I evaluates to {}".format(findLetter(I, dot, dash)))
	print("T evaluates to {}".format(findLetter(T, dot, dash)))
	print("Y evaluates to {}".format(findLetter(Y, dot, dash)))


main()
