#!/usr/bin/python3

import sys

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

byteCoins = {}

def calcByteCoins(left, right):
	if (left, right) in byteCoins:
		return byteCoins[(left, right)]
	x = [0]*n
	for i in range(0, n):
		x[i] = (left + (right * turns[i])) % mods[i]
	seq = ""
	for i in range(0, n):
		if i > 0:
			seq += " "
		seq += wheels[i][x[i]]
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
	byteCoins[(left, right)] = coin
	return coin

mins = {}
maxs = {}
#left, right: left must be in [-right, right]

def calcMins(left, right):
	if (left, right) in mins:
		return mins[(left, right)]
	if right == 0:
		mins[(left, right)] = 0
		return 0
	min1 = 999999999
	#(left, right) can be reached from (left-1, right-1), (left, right-1), (left+1, right-1)
	if abs(left-1) <= right-1:
		curmin = calcMins(left-1, right-1) + calcByteCoins(left, right)
		if curmin < min1:
			min1 = curmin
	if abs(left) <= right-1:
		curmin = calcMins(left, right-1) + calcByteCoins(left, right)
		if curmin < min1:
			min1 = curmin
	if abs(left+1) <= right-1:
		curmin = calcMins(left+1, right-1) + calcByteCoins(left, right)
		if curmin < min1:
			min1 = curmin
	mins[(left, right)] = min1
	return min1

def calcMaxs(left, right):
	if (left, right) in maxs:
		return maxs[(left, right)]
	if right == 0:
		maxs[(left, right)] = 0
		return 0
	max1 = 0
	#(left, right) can be reached from (left-1, right-1), (left, right-1), (left+1, right-1)
	if abs(left-1) <= right-1:
		curmax = calcMaxs(left-1, right-1) + calcByteCoins(left, right)
		if curmax > max1:
			max1 = curmax
	if abs(left) <= right-1:
		curmax = calcMaxs(left, right-1) + calcByteCoins(left, right)
		if curmax > max1:
			max1 = curmax
	if abs(left+1) <= right-1:
		curmax = calcMaxs(left+1, right-1) + calcByteCoins(left, right)
		if curmax > max1:
			max1 = curmax
	maxs[(left, right)] = max1
	return max1

pulls = 256
if pulls > 990: # just in case
	sys.setrecursionlimit(pulls+10)
minCoins = 999999999
maxCoins = 0
for i in range(-pulls, pulls+1):
	minCoin = calcMins(i, pulls)
	if minCoin < minCoins:
		minCoins = minCoin
	maxCoin = calcMaxs(i, pulls)
	if maxCoin > maxCoins:
		maxCoins = maxCoin
print(str(maxCoins)+' '+str(minCoins))