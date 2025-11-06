#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q03_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
crates = [int(x) for x in fileLines[0].split(',')]
crates.sort()
n = len(crates)
maxset = 0
cursize = 0
for i in range(0, n):
	if crates[i] > cursize:
		cursize = crates[i]
		maxset += cursize
print(maxset)
