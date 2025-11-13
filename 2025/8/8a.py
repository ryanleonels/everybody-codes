#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q08_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
steps = [int(x) for x in fileData.strip().split(',')]
n = len(steps)
nails = 32
passes = 0
for i in range(0, n - 1):
	if steps[i + 1] == steps[i] + (nails // 2) or steps[i + 1] == steps[i] - (nails // 2):
		passes += 1
print(passes)
