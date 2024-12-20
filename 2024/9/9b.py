#!/usr/bin/python3

import sys
sys.setrecursionlimit(2000)

beetles = {}

def beetle(n):
	if n == 0:
		return 0
	if n in beetles:
		return beetles[n]
	stamps = [1, 3, 5, 10, 15, 16, 20, 24, 25, 30]
	nStamps = len(stamps)
	minStamp = n + 1
	for i in range(0, nStamps):
		if n >= stamps[i]:
			stamp = beetle(n - stamps[i]) + 1
			if stamp < minStamp:
				minStamp = stamp
	beetles[n] = minStamp
	return minStamp

fileHandle = open("everybody_codes_e2024_q09_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
totalBeetles = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	brightness = int(fileLine)
	numBeetles = beetle(brightness)
	totalBeetles += numBeetles
print(totalBeetles)