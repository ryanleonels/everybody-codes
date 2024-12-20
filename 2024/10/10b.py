#!/usr/bin/python3

grid = []
totalPower = 0
fileHandle = open("everybody_codes_e2024_q10_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
x = 0
x1 = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		x += 1
		x1 = 0
		continue
	y = 0
	y1 = 0
	for i in range(0, len(fileLine)):
		if fileLine[i] == ' ':
			y += 1
		else:
			if len(grid) == x:
				grid.append([])
			if len(grid[x]) == y:
				grid[x].append([])
			if len(grid[x][y]) == x1:
				grid[x][y].append([])
			grid[x][y][x1].append(fileLine[i])
	x1 += 1
for x in range(0, len(grid)):
	for y in range(0, len(grid[x])):
		grid1 = grid[x][y]
		row = len(grid1)
		col = len(grid1[0])
		runicWord = ''
		for i in range(0, row):
			for j in range(0, col):
				if grid1[i][j] == '.':
					ch = ''
					for k in range(65, 91):
						if chr(k) in grid1[i]:
							found = False
							for l in range(0, row):
								if grid1[l][j] == chr(k):
									found = True
									ch = chr(k)
									break
							if found == True:
								runicWord += ch
								break
		power = 0
		for i in range(0, len(runicWord)):
			power += ((i + 1) * (ord(runicWord[i]) - 64))
		totalPower += power
print(totalPower)