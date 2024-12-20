#!/usr/bin/python3

blocks = 0
n = 0
grid = []
fileHandle = open("everybody_codes_e2024_q03_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
row = len(fileLines)
col = len(fileLines[0])
for i in range(0, row):
	grid.append([])
	for j in range(0, col):
		if fileLines[i][j] == '#':
			grid[i].append(1)
			n += 1
		else:
			grid[i].append(0)
depth = 1
while n != 0:
	n = 0
	for i in range(1, row - 1):
		for j in range(1, col - 1):
			if grid[i][j] >= depth and grid[i-1][j] >= depth and grid[i+1][j] >= depth and grid[i][j-1] >= depth and grid[i][j+1] >= depth and grid[i-1][j-1] >= depth and grid[i-1][j+1] >= depth and grid[i+1][j-1] >= depth and grid[i+1][j+1] >= depth:
				grid[i][j] = depth + 1
				n += 1
	depth += 1
for i in range(0, row):
	for j in range(0, col):
		blocks += grid[i][j]
print(blocks)