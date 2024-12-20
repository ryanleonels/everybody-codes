#!/usr/bin/python3

grid = []
totalPower = 0
fileHandle = open("everybody_codes_e2024_q10_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))
row = len(grid)
col = len(grid[0])
x = row // 6
y = col // 6
improved = True
while improved == True:
	improved = False
	for x1 in range(0, x):
		for y1 in range(0, y):
			missing = False
			for i in range(2, 6):
				for j in range(2, 6):
					if grid[(x1*6)+i][(y1*6)+j] == '.':
						rowSymbols = set()
						rowSymbols.add(grid[(x1*6)+i][(y1*6)])
						rowSymbols.add(grid[(x1*6)+i][(y1*6)+1])
						rowSymbols.add(grid[(x1*6)+i][(y1*6)+6])
						rowSymbols.add(grid[(x1*6)+i][(y1*6)+7])
						colSymbols = set()
						colSymbols.add(grid[(x1*6)][(y1*6)+j])
						colSymbols.add(grid[(x1*6)+1][(y1*6)+j])
						colSymbols.add(grid[(x1*6)+6][(y1*6)+j])
						colSymbols.add(grid[(x1*6)+7][(y1*6)+j])
						symbol1 = []
						for symbol in rowSymbols:
							if symbol in colSymbols:
								if symbol != '?':
									symbol1.append(symbol)
						if len(symbol1) >= 1:
							improved = True
							grid[(x1*6)+i][(y1*6)+j] = symbol1[0]
						else:
							missing = True
			if missing == True:
				for i in range(2, 6):
					for j in range(2, 6):
						if grid[(x1*6)+i][(y1*6)+j] == '.':
							symbols = {}
							rowSymbols = set()
							for k in range(0, 8):
								rowSymbol = grid[(x1*6)+i][(y1*6)+k]
								if rowSymbol != '.':
									rowSymbols.add(rowSymbol)
									if rowSymbol in symbols:
										symbols[rowSymbol] += 1
									else:
										symbols[rowSymbol] = 1
							colSymbols = set()
							for k in range(0, 8):
								colSymbol = grid[(x1*6)+k][(y1*6)+j]
								if colSymbol != '.':
									colSymbols.add(colSymbol)
									if colSymbol in symbols:
										symbols[colSymbol] += 1
									else:
										symbols[colSymbol] = 1
							if '?' in rowSymbols and symbols['?'] == 1:
								#print([x1, y1, i, j, 0])
								symbol1 = []
								for symbol in symbols:
									if symbols[symbol] == 1 and symbol != '?':
										symbol1.append(symbol)
								if len(symbol1) == 1:
									symbol2 = symbol1[0]
									grid[(x1*6)+i][(y1*6)+j] = symbol2
									improved = True
									for k in range(0, 8):
										rowSymbol = grid[(x1*6)+i][(y1*6)+k]
										if rowSymbol == '?':
											grid[(x1*6)+i][(y1*6)+k] = symbol2
							if '?' in colSymbols and symbols['?'] == 1:
								#print([x1, y1, i, j, 1])
								symbol1 = []
								for symbol in symbols:
									if symbols[symbol] == 1 and symbol != '?':
										symbol1.append(symbol)
								if len(symbol1) == 1:
									symbol2 = symbol1[0]
									grid[(x1*6)+i][(y1*6)+j] = symbol2
									improved = True
									for k in range(0, 8):
										colSymbol = grid[(x1*6)+k][(y1*6)+j]
										if colSymbol == '?':
											grid[(x1*6)+k][(y1*6)+j] = symbol2
#for line in grid:
	#print(''.join(line))
for x1 in range(0, x):
	#pows = []
	for y1 in range(0, y):
		solved = True
		for i in range(2, 6):
			for j in range(2, 6):
				if grid[(x1*6)+i][(y1*6)+j] == '.':
					solved = False
		power = 0
		if solved == True:
			for i in range(2, 6):
				for j in range(2, 6):
					pos = ((i - 2) * 4) + (j - 2) + 1
					ch = ord(grid[(x1*6)+i][(y1*6)+j]) - 64
					power += (pos * ch)
		#pows.append(power)
		totalPower += power
	#print(pows)
print(totalPower)