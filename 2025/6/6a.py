#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q06_p1.txt", "r")
fileData = fileHandle.read().strip()
n = len(fileData)
(mentors, pairs) = (0, 0)
for i in range(0, n):
	if fileData[i] == 'A':
		mentors += 1
	if fileData[i] == 'a':
		pairs += mentors
print(pairs)
