#!/usr/bin/python3

import sys
sys.setrecursionlimit(30000)

beetles = {}

def beetle(n):
	if n == 0:
		return 0
	if n in beetles:
		return beetles[n]
	stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30, 37, 38, 49, 50, 74, 75, 100, 101]
	nStamps = len(stamps)
	minStamp = n + 1
	for i in range(0, nStamps):
		if n >= stamps[i]:
			stamp = beetle(n - stamps[i]) + 1
			if stamp < minStamp:
				minStamp = stamp
	beetles[n] = minStamp
	return minStamp

fileHandle = open("everybody_codes_e2024_q09_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
minBeetles = 0
maxBrightness = 0
brightnesses = []
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	brightness = int(fileLine)
	if brightness > maxBrightness:
		maxBrightness = brightness
	brightnesses.append(brightness)
n = len(brightnesses)
for i in range(1, maxBrightness+1):
	beetle(i)
for i in range(0, n):
	brightness = brightnesses[i]
	b1 = brightness // 2
	b2 = brightness - b1
	minBeetle = maxBrightness
	while b2 - b1 <= 100:
		beetleCount = beetle(b1) + beetle(b2)
		if beetleCount < minBeetle:
			minBeetle = beetleCount
		(b1, b2) = (b1 - 1, b2 + 1)
	minBeetles += minBeetle
print(minBeetles)