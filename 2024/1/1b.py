#!/usr/bin/python3

potions = 0
fileHandle = open("everybody_codes_e2024_q01_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	n = len(fileLine)
	for i in range(0, n, 2):
		if fileLine[i] == 'B':
			potions += 1
		if fileLine[i] == 'C':
			potions += 3
		if fileLine[i] == 'D':
			potions += 5
		if fileLine[i+1] == 'B':
			potions += 1
		if fileLine[i+1] == 'C':
			potions += 3
		if fileLine[i+1] == 'D':
			potions += 5
		if fileLine[i] != 'x' and fileLine[i+1] != 'x':
			potions += 2
print(potions)
