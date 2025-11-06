#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q03_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
crates = [int(x) for x in fileLines[0].split(',')]
crates.sort()
n = len(crates)
minset = 0
cursize = 0
n1 = 0
for i in range(0, n):
	if crates[i] > cursize:
		cursize = crates[i]
		minset += cursize
		n1 += 1
		if n1 == 20:
			break
print(minset)
