#!/usr/bin/python3

n = 0
turns = []
wheels = []
fileHandle = open("everybody_codes_e2024_q16_p1.txt", "r")
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
seq = ""
for i in range(0, n):
	if i > 0:
		seq += " "
	seq += wheels[i][(turns[i] * 100) % mods[i]]
print(seq)