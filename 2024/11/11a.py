#!/usr/bin/python3

termites = {'A': 1}
growth = {}
fileHandle = open("everybody_codes_e2024_q11_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	ch = fileLine.split(':')[0]
	growth[ch] = fileLine.split(':')[1].split(',')
for i in range(0, 4):
	termites1 = {}
	for termite in termites:
		n = termites[termite]
		for ch in growth[termite]:
			if ch in termites1:
				termites1[ch] += n
			else:
				termites1[ch] = n
	termites = termites1
n = 0
for termite in termites:
	n += termites[termite]
print(n)