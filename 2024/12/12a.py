#!/usr/bin/python3

value = 0
targets = []
fileHandle = open("everybody_codes_e2024_q12_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nrow = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	nrow += 1
row = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	n = len(fileLine)
	for i in range(0, n):
		if fileLine[i] == 'T':
			targets.append(i + (nrow - row - 2))
	row += 1
n = len(targets)
for i in range(0, n):
	if (targets[i] - 1) % 3 == 0:
		value += ((targets[i] - 1) / 3)
	if (targets[i] - 1) % 3 == 1:
		value += ((targets[i] - 2) / 3) * 2
	if (targets[i] - 1) % 3 == 2:
		value += ((targets[i] - 3) / 3) * 3
print(int(value))