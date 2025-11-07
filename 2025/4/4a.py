#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q04_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
gears = [int(x) for x in fileLines]
print(2025 * gears[0] // gears[-1])
