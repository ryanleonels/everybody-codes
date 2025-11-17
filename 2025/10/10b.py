#!/usr/bin/python3

grid = []
dragon = (-1, -1)
dRange = {}
sheeps = set()
sRange = {}
hideouts = set()
fileHandle = open("everybody_codes_e2025_q10_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
row = len(grid)
col = len(grid[0])
for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] == 'D':
			dragon = (i, j)
		if grid[i][j] == 'S':
			sheeps.add((i, j))
		if grid[i][j] == '#':
			hideouts.add((i, j))
dRange[0] = set()
dRange[0].add(dragon)
sRange[0] = set()
for sheep in sheeps:
	sRange[0].add(sheep)
moves = 20
nEat = 0
for move in range(0, moves):
	dRange[move + 1] = set()
	for (i, j) in dRange[move]:
		(i1, j1) = (i - 2, j - 1)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
		(i1, j1) = (i - 2, j + 1)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
		(i1, j1) = (i - 1, j - 2)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
		(i1, j1) = (i - 1, j + 2)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
		(i1, j1) = (i + 1, j - 2)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
		(i1, j1) = (i + 1, j + 2)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
		(i1, j1) = (i + 2, j - 1)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
		(i1, j1) = (i + 2, j + 1)
		if i >= 0 and i < row and j >= 0 and j < col:
			dRange[move + 1].add((i1, j1))
	for (i, j) in dRange[move + 1]:
		if (i, j) in sRange[move] and (i, j) not in hideouts:
			nEat += 1
			sRange[move].remove((i, j))
	sRange[move + 1] = set()
	for (i, j) in sRange[move]:
		if i < row - 1:
			sRange[move + 1].add((i + 1, j))
	for (i, j) in dRange[move + 1]:
		if (i, j) in sRange[move + 1] and (i, j) not in hideouts:
			nEat += 1
			sRange[move + 1].remove((i, j))
print(nEat)
