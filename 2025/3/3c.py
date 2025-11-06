#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q03_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
crates = [int(x) for x in fileLines[0].split(',')]
crates.sort()
n = len(crates)
(curcopy, maxcopy) = (0, 1)
cursize = 0
n1 = 0
for i in range(0, n):
	if crates[i] > cursize:
		cursize = crates[i]
		curcopy = 1
	else:
		curcopy += 1
		if curcopy > maxcopy:
			maxcopy = curcopy
print(maxcopy)
