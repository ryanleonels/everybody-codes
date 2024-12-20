#!/usr/bin/python3

lengths = []
minLength = 999999999
minStrike = 999999999999999
fileHandle = open("everybody_codes_e2024_q04_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
n = len(fileLines)
for i in range(0, n):
	lengths.append(int(fileLines[i]))
for i in range(0, n):
	strikes = 0
	for j in range(0, n):
		strikes += abs(lengths[i] - lengths[j])
	if strikes < minStrike:
		minStrike = strikes
print(minStrike)