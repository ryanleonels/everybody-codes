#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q06_p3.txt", "r")
fileData = fileHandle.read().strip()
n = len(fileData)
(rep, dlim) = (1000, 1000)
pairs = [0, 0, 0]
for i in range(0, n):
	if fileData[i] >= 'a' and fileData[i] <= 'c':
		ch = ord(fileData[i]) - ord('a')
		for j in range(-dlim, dlim + 1):
			pos = (i + j) % n
			loop = (i + j) // n
			rep1 = rep - abs(loop)
			if fileData[pos] >= 'A' and fileData[pos] <= 'C':
				ch1 = ord(fileData[pos]) - ord('A')
				if ch == ch1:
					pairs[ch] += rep1
print(sum(pairs))
