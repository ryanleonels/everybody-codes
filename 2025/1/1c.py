#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q01_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
names = fileLines[0].split(',')
instructions = fileLines[2].split(',')
(n, n1, pos) = (len(names), len(instructions), 0)
for i in range(0, n1):
	step = int(instructions[i][1:])
	if instructions[i][0] == 'L':
		step = -step
	pos = (step % n)
	temp = names[0]
	names[0] = names[pos]
	names[pos] = temp
print(names[0])
