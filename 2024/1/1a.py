#!/usr/bin/python3

potions = 0
fileHandle = open("everybody_codes_e2024_q01_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	n = len(fileLine)
	for i in range(0, n):
		if fileLine[i] == 'B':
			potions += 1
		if fileLine[i] == 'C':
			potions += 3
print(potions)
