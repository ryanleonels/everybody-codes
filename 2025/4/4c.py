#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q04_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = len(fileLines)
gears = []
for i in range(0, n - 1):
	gears.append((int(fileLines[i].split('|')[-1]), int(fileLines[i + 1].split('|')[0])))
x = 100
for i in range(0, n - 1):
	x *= (gears[i][0] / gears[i][1])
print(int(x))
