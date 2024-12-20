#!/usr/bin/python3

potions = 0
fileHandle = open("everybody_codes_e2024_q01_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	n = len(fileLine)
	for i in range(0, n, 3):
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
		if fileLine[i+2] == 'B':
			potions += 1
		if fileLine[i+2] == 'C':
			potions += 3
		if fileLine[i+2] == 'D':
			potions += 5
		x = 0
		if fileLine[i] != 'x':
			x += 1
		if fileLine[i+1] != 'x':
			x += 1
		if fileLine[i+2] != 'x':
			x += 1
		if x == 2:
			potions += 2
		if x == 3:
			potions += 6
print(potions)
