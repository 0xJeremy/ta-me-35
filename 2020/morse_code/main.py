#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

import random
import math
import time

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
	mmin = int(cMin * 1000)
	mmax = int(cMax * 1000)
	return [random.randint(mmin, mmax)/1000 for i in range(k)]

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
		if Button.CENTER in brick.buttons():
			return data
		if tsensor.pressed():
			if not down:
				down = True
				start = time.time()
		else:
			if down:
				data.append(time.time() - start)
				print("New data: {}".format(data[-1]))
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
	print("Translation is: {}".format(translation))
	for key in MORSE_CODE:
		if translation == MORSE_CODE[key]:
			return key
	return None

########################
### DISPLAY FUNCTION ###
########################

def display(message):
	brick.display.clear()
	brick.display.text(message)

#####################
### MAIN FUNCTION ###
#####################

def main():
	display("Please enter training data")
	touchSensor = TouchSensor(Port.S1)
	training_data = GetDataArray(touchSensor)
	clusters = CalculateMeans(2, training_data)

	dot = min(clusters)
	dash = max(clusters)

	print("Dot length: {} sec".format(dot))
	print("Dash length: {} sec".format(dash))

	while True:
		if Button.LEFT in brick.buttons():
			break
		letter = findLetter(GetDataArray(touchSensor), dot, dash)
		if letter is None:
			print("LETTER NOT FOUND")
			display("Not found")
		else:
			print("THE LETTER IS: {}".format(letter))
			display("The letter is: {}".format(letter))
		wait(0.5)


main()
