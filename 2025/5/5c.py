#!/usr/bin/python3

swords = []
fileHandle = open("everybody_codes_e2025_q05_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
nLines = len(fileLines)
for line in range(0, nLines):
	id1 = int(fileLines[line].split(':')[0])
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
	quality = ""
	fishbones = []
	for i in range(0, n1):
		quality += str(fishbone[i][0])
		fishbone1 = ""
		if fishbone[i][1] != None:
			fishbone1 = str(fishbone[i][1])
		fishbone1 += str(fishbone[i][0])
		if fishbone[i][2] != None:
			fishbone1 += str(fishbone[i][2])
		fishbone1 = int(fishbone1)
		fishbones.append(fishbone1)
	quality = int(quality)
	swords.append({'id1': id1, 'quality': quality, 'fishbones': fishbones})
#for sword in swords:
	#print(sword)
pos = [None] * nLines
for i in range(0, nLines):
	pos1 = 0
	for j in range(0, nLines):
		if i != j:
			status = 0 # 1 = i stronger than j, -1 = i weaker than j, 0 = not yet determined
			if swords[i]['quality'] > swords[j]['quality']:
				status = 1
			if swords[i]['quality'] < swords[j]['quality']:
				status = -1
			if status == 0:
				k = 0
				while k < len(swords[i]['fishbones']) and swords[i]['fishbones'][k] == swords[j]['fishbones'][k]:
					k += 1
				if k < len(swords[i]['fishbones']) and swords[i]['fishbones'][k] > swords[j]['fishbones'][k]:
					status = 1
				if k < len(swords[i]['fishbones']) and swords[i]['fishbones'][k] < swords[j]['fishbones'][k]:
					status = -1
				if status == 0:
					if swords[i]['id1'] > swords[j]['id1']:
						status = 1
					if swords[i]['id1'] < swords[j]['id1']:
						status = -1
			if status == -1:
				pos1 += 1
	pos[pos1] = swords[i]['id1']
#print(pos)
checksum = 0
for i in range(0, nLines):
	checksum += (pos[i] * (i + 1))
print(checksum)
