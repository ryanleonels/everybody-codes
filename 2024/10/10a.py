#!/usr/bin/python3

grid = []
fileHandle = open("everybody_codes_e2024_q10_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
row = len(grid)
col = len(grid[0])
runicWord = ''
for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] == '.':
			ch = ''
			for k in range(65, 91):
				if chr(k) in grid[i]:
					found = False
					for l in range(0, row):
						if grid[l][j] == chr(k):
							found = True
							ch = chr(k)
							break
					if found == True:
						runicWord += ch
						break
print(runicWord)