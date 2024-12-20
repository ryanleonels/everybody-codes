#!/usr/bin/python3

segments = set()
fileHandle = open("everybody_codes_e2024_q14_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	steps = fileLine.split(',')
	segment = (0, 0, 0)
	for step in steps:
		direction = step[0]
		num = int(step[1:])
		if direction == 'U':
			for i in range(0, num):
				segment = (segment[0] + 1, segment[1], segment[2])
				segments.add(segment)
		if direction == 'D':
			for i in range(0, num):
				segment = (segment[0] - 1, segment[1], segment[2])
				segments.add(segment)
		if direction == 'R':
			for i in range(0, num):
				segment = (segment[0], segment[1] + 1, segment[2])
				segments.add(segment)
		if direction == 'L':
			for i in range(0, num):
				segment = (segment[0], segment[1] - 1, segment[2])
				segments.add(segment)
		if direction == 'F':
			for i in range(0, num):
				segment = (segment[0], segment[1], segment[2] + 1)
				segments.add(segment)
		if direction == 'B':
			for i in range(0, num):
				segment = (segment[0], segment[1], segment[2] - 1)
				segments.add(segment)
print(len(segments))