#!/usr/bin/python3

def isChild(child, parent1, parent2):
	for i in range(0, len(child)):
		if child[i] != parent1[i] and child[i] != parent2[i]:
			return False
	return True

fileHandle = open("everybody_codes_e2025_q09_p3.txt", "r")
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
connections = set()
for child in range(1, n + 1):
	for parent1 in range(1, n):
		for parent2 in range(parent1 + 1, n):
			if child != parent1 and child != parent2:
				if isChild(dnas[child], dnas[parent1], dnas[parent2]):
					print(child, parent1, parent2)
					(a, b, c) = sorted([child, parent1, parent2])
					connections.add((a, b))
					connections.add((a, c))
					connections.add((b, c))
allConnected = False
while not allConnected:
	allConnected = True
	for i in range(1, n + 1):
		for j in range(i + 1, n + 1):
			for k in range(j + 1, n + 1):
				if (i, j) in connections and (i, k) in connections and (j, k) not in connections:
					connections.add((j, k))
					allConnected = False
				if (i, j) in connections and (j, k) in connections and (i, k) not in connections:
					connections.add((i, k))
					allConnected = False
				if (i, k) in connections and (j, k) in connections and (i, j) not in connections:
					connections.add((i, j))
					allConnected = False
group = {}
for i in range(1, n + 1):
	group[i] = i
for i in range(1, n):
	for j in range(i + 1, n + 1):
		if (i, j) in connections:
			print(i, j)
			group[j] = group[i]
print(group)
groups = {}
for i in range(1, n + 1):
	g = group[i]
	if g not in groups:
		groups[g] = set()
	groups[g].add(i)
print(groups)
(cursize, maxsize, maxgroup, scalesum) = (0, 0, 0, 0)
for g in groups:
	cursize = len(groups[g])
	if cursize > maxsize:
		maxsize = cursize
		maxgroup = groups[g]
		scalesum = sum(groups[g])
print(maxgroup)
print(scalesum)
