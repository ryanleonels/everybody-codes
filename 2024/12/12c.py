#!/usr/bin/python3

totalRank = 0
targets = []
fileHandle = open("everybody_codes_e2024_q12_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nrow = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	(x, y) = (int(fileLine.split(' ')[0]), int(fileLine.split(' ')[1]))
	hitx = x // 2
	hity = y - (x - (x // 2))
	minRank = 99999999
	for i in range(1, hitx + 1):
		# calculate y1 when hitx is reached at power i
		#A
		if hitx <= i:
			y1 = hitx
		if hitx > i and hitx <= i * 2:
			y1 = i
		if hitx > i * 2:
			y1 = i - (hitx - (i * 2))
		if y1 == hity:
			rank = i
			if rank < minRank:
				minRank = rank
		#B
		if hitx <= i:
			y1 = hitx + 1
		if hitx > i and hitx <= i * 2:
			y1 = i + 1
		if hitx > i * 2:
			y1 = i - (hitx - (i * 2)) + 1
		if y1 == hity:
			rank = i * 2
			if rank < minRank:
				minRank = rank
		#C
		if hitx <= i:
			y1 = hitx + 2
		if hitx > i and hitx <= i * 2:
			y1 = i + 2
		if hitx > i * 2:
			y1 = i - (hitx - (i * 2)) + 2
		if y1 == hity:
			rank = i * 3
			if rank < minRank:
				minRank = rank
	if minRank != 99999999:
		totalRank += minRank
print(totalRank)
