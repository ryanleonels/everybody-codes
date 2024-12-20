#!/usr/bin/python3

maxn = 0
number = '0000'
number2024 = '0000'
numbers = {}
grid = []
fileHandle = open("everybody_codes_e2024_q05_p2.txt", "r")
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
i = 0
while True:
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
	i += 1
	if number in numbers:
		numbers[number] += 1
		if numbers[number] > maxn:
			maxn = numbers[number]
			print([maxn, number, i])
		if numbers[number] == 2024:
			number2024 = number
			break
	else:
		numbers[number] = 1
print(number2024)
print(i)
print(int(number2024) * int(i))