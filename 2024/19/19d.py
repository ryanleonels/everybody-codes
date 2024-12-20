#!/usr/bin/python3

key = ""
grid = []
rounds = 1024
firstLine = True
fileHandle = open("everybody_codes_e2024_q19_p4.txt", "r")
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

maps = {} # transform maps after n = 2^k turns, maps[n][(x, y)] = (i, j) where (x, y) will be after n turns
maps0 = []
for i in range(0, row):
	maps0.append([])
	for j in range(0, col):
		maps0[i].append((i, j))
maps1 = [] # do transform once
for i in range(0, row):
	maps1.append([])
	for j in range(0, col):
		maps1[i].append(maps0[i][j])
for i in range(1, row - 1):
	for j in range(1, col - 1):
		k = ((i - 1) * (col - 2)) + (j - 1)
		ch = key[k % n]
		a = maps1[i-1][j-1]
		b = maps1[i-1][j]
		c = maps1[i-1][j+1]
		d = maps1[i][j+1]
		e = maps1[i+1][j+1]
		f = maps1[i+1][j]
		g = maps1[i+1][j-1]
		h = maps1[i][j-1]
		if ch == 'R':
			maps1[i-1][j-1] = h
			maps1[i-1][j] = a
			maps1[i-1][j+1] = b
			maps1[i][j+1] = c
			maps1[i+1][j+1] = d
			maps1[i+1][j] = e
			maps1[i+1][j-1] = f
			maps1[i][j-1] = g
		if ch == 'L':
			maps1[i-1][j-1] = b
			maps1[i-1][j] = c
			maps1[i-1][j+1] = d
			maps1[i][j+1] = e
			maps1[i+1][j+1] = f
			maps1[i+1][j] = g
			maps1[i+1][j-1] = h
			maps1[i][j-1] = a
maps[1] = {}
for i in range(0, row):
	for j in range(0, col):
		maps[1][maps1[i][j]] = (i, j)
n = 2
while n <= rounds: # for maps[2n], do maps[n] twice
	n2 = n // 2
	maps[n] = {}
	for cell in maps[n2]: #maps[2n][(x, y)] = maps[n][maps[n][(x, y)]]
		maps[n][cell] = maps[n2][maps[n2][cell]]
	n *= 2

x = rounds
while x > 0:
	x1 = 1
	while x1 * 2 <= x:
		x1 *= 2
	#print(x1) # do x1 rounds transformation of grid -> grid1
	grid1 = []
	for i in range(0, row):
		grid1.append([])
		for j in range(0, col):
			grid1[i].append(grid[i][j])
	for i in range(0, row):
		for j in range(0, col):
			grid1[maps[x1][(i, j)][0]][maps[x1][(i, j)][1]] = grid[i][j]
	grid = grid1
	x -= x1

for i in range(0, row):
	print(''.join(grid[i]))
