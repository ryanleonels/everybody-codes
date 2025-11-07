#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q04_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
gears = [int(x) for x in fileLines]
turns = 10000000000000 * gears[-1] // gears[0]
if 10000000000000 * gears[-1] % gears[0] != 0:
	turns += 1
print(turns)
