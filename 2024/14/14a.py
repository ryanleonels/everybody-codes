#!/usr/bin/python3

h = 0
hmax = 0
fileHandle = open("everybody_codes_e2024_q14_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
steps = fileData.split(',')
for step in steps:
	direction = step[0]
	num = int(step[1:])
	if direction == 'U':
		h += num
	if direction == 'D':
		h -= num
	if h > hmax:
		hmax = h
print(hmax)