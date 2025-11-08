#!/usr/bin/python3

(qmin, qmax) = (10 ** 308, 0)
fileHandle = open("everybody_codes_e2025_q05_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nLines = len(fileLines)
for line in range(0, nLines):
	quality = ""
	numbers = [int(x) for x in fileLines[line].split(':')[1].split(',')]
	n = len(numbers)
	(n1, fishbone) = (0, [])
	for i in range(0, n):
		j = 0
		placed = False
		while j < n1 and not placed:
			if numbers[i] < fishbone[j][0] and fishbone[j][1] == None:
				placed = True
				fishbone[j][1] = numbers[i]
				continue
			if numbers[i] > fishbone[j][0] and fishbone[j][2] == None:
				placed = True
				fishbone[j][2] = numbers[i]
				continue
			j += 1
		if j == n1 and not placed:
			n1 += 1
			fishbone.append([numbers[i], None, None])
	for i in range(0, n1):
		quality += str(fishbone[i][0])
	quality = int(quality)
	if quality < qmin:
		qmin = quality
	if quality > qmax:
		qmax = quality
print(qmax - qmin)
