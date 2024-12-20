#!/usr/bin/python3

strikes = 0
lengths = []
minLength = 999999999
fileHandle = open("everybody_codes_e2024_q04_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = len(fileLines)
for i in range(0, n):
	lengths.append(int(fileLines[i]))
	if lengths[i] < minLength:
		minLength = lengths[i]
for i in range(0, n):
	strikes += (lengths[i] - minLength)
print(strikes)