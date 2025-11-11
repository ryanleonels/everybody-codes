#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q06_p2.txt", "r")
fileData = fileHandle.read().strip()
n = len(fileData)
mentors = [0, 0, 0]
pairs = [0, 0, 0]
for i in range(0, n):
	if fileData[i] >= 'A' and fileData[i] <= 'C':
		mentors[ord(fileData[i]) - ord('A')] += 1
	if fileData[i] >= 'a' and fileData[i] <= 'c':
		pairs[ord(fileData[i]) - ord('a')] += mentors[ord(fileData[i]) - ord('a')]
print(sum(pairs))
