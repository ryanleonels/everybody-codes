#!/usr/bin/python3

n = 0
turns = []
wheels = []
fileHandle = open("everybody_codes_e2024_q16_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
isSequence = False
for fileLine in fileLines:
	if fileLine.strip() == '':
		isSequence = True
		for i in range(0, n):
			wheels.append([])
		continue
	if isSequence == False:
		turns = [int(x) for x in fileLine.split(',')]
		n = len(turns)
	if isSequence == True:
		n1 = (len(fileLine) + 1) // 4
		for i in range(0, n1):
			face = fileLine[(i*4):(i*4)+3]
			if face.strip() != '':
				wheels[i].append(face)
mods = []
for i in range(0, n):
	mods.append(len(wheels[i]))
x = tuple([0]*n)
pos = {}
pos[x] = 0
i = 0
cycleStart = 0
cycleLen = 0
coins = []
coins.append(0)
while i <= 202420242024:
	i += 1
	x1 = [0]*n
	for j in range(0, n):
		x1[j] = (x[j] + turns[j]) % mods[j]
	x = tuple(x1)
	seq = ""
	for j in range(0, n):
		if j > 0:
			seq += " "
		seq += wheels[j][x[j]]
	chars = {}
	for j in range(0, n * 4, 2):
		ch = seq[j]
		if ch in chars:
			chars[ch] += 1
		else:
			chars[ch] = 1
	coin = 0
	for char in chars:
		if chars[char] >= 3:
			coin += (chars[char] - 2)
	coins.append(coins[i-1] + coin)
	if x in pos:
		cycleStart = pos[x]
		cycleLen = i - pos[x]
		#print("step " + str(i) + " = step " + str(pos[x]) + " = " + str(x))
		break
	pos[x] = i
#print(cycleStart)
#print(cycleLen)
cycleNum = 202420242024 // cycleLen
cycleMod = 202420242024 % cycleLen
totalCoins = (coins[cycleLen] * cycleNum) + coins[cycleMod]
print(totalCoins)