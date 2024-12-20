#!/usr/bin/python3

fileHandle = open("everybody_codes_e2024_q09_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
totalBeetles = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	brightness = int(fileLine)
	beetles = brightness // 10
	brightness1 = brightness % 10
	if brightness1 >= 5:
		beetles += 1
		brightness1 -= 5
	if brightness1 >= 3:
		beetles += 1
		brightness1 -= 3
	beetles += brightness1
	totalBeetles += beetles
print(totalBeetles)