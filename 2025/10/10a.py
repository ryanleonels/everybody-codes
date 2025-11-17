#!/usr/bin/python3

grid = []
dragon = (-1, -1)
dRange = {}
sheeps = set()
fileHandle = open("everybody_codes_e2025_q10_p1.txt", "r")
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
dRange[0] = set()
dRange[0].add(dragon)
for move in range(0, 4):
	dRange[move + 1] = set()
	for (i, j) in dRange[move]:
		dRange[move + 1].add((i, j))
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
nSheep = 0
for (i, j) in sheeps:
	if (i, j) in dRange[4]:
		nSheep += 1
print(nSheep)
