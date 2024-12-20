#!/usr/bin/python3

number = '0000'
grid = []
fileHandle = open("everybody_codes_e2024_q05_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = len(fileLines)
for i in range(0, n):
	grid.append([int(x) for x in fileLines[i].split(' ')])
columns = [[], [], [], []]
for i in range(0, n):
	for j in range(0, 4):
		columns[j].append(grid[i][j])
for i in range(0, 10):
	col = i % 4
	clapper = columns[col][0]
	columns[col] = columns[col][1:]
	col = (col + 1) % 4
	row = -1
	clapdir = 1
	for j in range(0, clapper):
		movedRight = False
		if clapdir == 1 and row == len(columns[col]) - 1:
			col = (col + 1) % 4
			clapdir = -1
			movedRight = True
		if clapdir == -1 and row == 0 and movedRight == False:
			col = (col - 1) % 4
			clapdir = 1
			movedRight = True
		if movedRight == False:
			row += clapdir
	if clapdir == 1:
		columns[col].insert(row, clapper)
	if clapdir == -1:
		col = (col - 1) % 4
		columns[col].insert(row + 1, clapper)
	number = str(columns[0][0]) + str(columns[1][0]) + str(columns[2][0]) + str(columns[3][0])
print(number)
