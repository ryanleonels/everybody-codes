#!/usr/bin/python3

key = ""
message = ""
grid = []
firstLine = True
fileHandle = open("everybody_codes_e2024_q19_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		firstLine = False
		continue
	if firstLine == True:
		key = fileLine
	else:
		grid.append(list(fileLine))

n = len(key)
row = len(grid)
col = len(grid[0])
for n1 in range(0, 100):
	for i in range(1, row - 1):
		for j in range(1, col - 1):
			k = ((i - 1) * (col - 2)) + (j - 1)
			ch = key[k % n]
			a = grid[i-1][j-1]
			b = grid[i-1][j]
			c = grid[i-1][j+1]
			d = grid[i][j+1]
			e = grid[i+1][j+1]
			f = grid[i+1][j]
			g = grid[i+1][j-1]
			h = grid[i][j-1]
			if ch == 'R':
				grid[i-1][j-1] = h
				grid[i-1][j] = a
				grid[i-1][j+1] = b
				grid[i][j+1] = c
				grid[i+1][j+1] = d
				grid[i+1][j] = e
				grid[i+1][j-1] = f
				grid[i][j-1] = g
			if ch == 'L':
				grid[i-1][j-1] = b
				grid[i-1][j] = c
				grid[i-1][j+1] = d
				grid[i][j+1] = e
				grid[i+1][j+1] = f
				grid[i+1][j] = g
				grid[i+1][j-1] = h
				grid[i][j-1] = a

msg = False
for i in range(1, row - 1):
	for j in range(1, col - 1):
		ch = grid[i][j]
		if ch == '>':
			msg = True
		else:
			if ch == '<':
				msg = False
			else:
				if msg == True:
					message += grid[i][j]

print(message)
for i in range(0, row):
	print(''.join(grid[i]))