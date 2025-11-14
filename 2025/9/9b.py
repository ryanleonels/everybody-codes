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

fileHandle = open("everybody_codes_e2025_q09_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
dnas = {}
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(num, dna) = fileLine.split(':')
	dnas[int(num)] = dna
n = len(dnas)
total = 0
for child in range(1, n + 1):
	for parent1 in range(1, n):
		for parent2 in range(parent1 + 1, n):
			if child != parent1 and child != parent2:
				if isChild(dnas[child], dnas[parent1], dnas[parent2]):
					similarity = similar(dnas[child], dnas[parent1], dnas[parent2])
					#print(child, parent1, parent2, similarity)
					total += similarity
print(total)
