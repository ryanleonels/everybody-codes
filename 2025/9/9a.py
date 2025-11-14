#!/usr/bin/python3

def isChild(child, parent1, parent2):
	for i in range(0, len(child)):
		if child[i] != parent1[i] and child[i] != parent2[i]:
			return False
	return True

def similar(child, parent1, parent2):
	(similar1, similar2) = (0, 0)
	for i in range(0, len(child)):
		if child[i] == parent1[i]:
			similar1 += 1
		if child[i] == parent2[i]:
			similar2 += 1
	return similar1 * similar2

fileHandle = open("everybody_codes_e2025_q09_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
dnas = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(num, dna) = fileLine.split(':')
	dnas[num] = dna
(child, similarity) = ('0', 0)
if isChild(dnas['1'], dnas['2'], dnas['3']):
	child = '1'
	similarity = similar(dnas['1'], dnas['2'], dnas['3'])
if isChild(dnas['2'], dnas['1'], dnas['3']):
	child = '2'
	similarity = similar(dnas['2'], dnas['1'], dnas['3'])
if isChild(dnas['3'], dnas['1'], dnas['2']):
	child = '3'
	similarity = similar(dnas['3'], dnas['1'], dnas['2'])
print(similarity)
