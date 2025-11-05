#!/usr/bin/python3

import math

def add(x1, y1, x2, y2):
	return (x1 + x2, y1 + y2)

def mul(x1, y1, x2, y2):
	return ((x1 * x2) - (y1 * y2), (x1 * y2) + (y1 * x2))

def div(x1, y1, x2, y2):
	(z1, z2) = (x1 / x2, y1 / y2)
	return (math.floor(z1) if z1 > 0 else math.ceil(z1), math.floor(z2) if z2 > 0 else math.ceil(z2))

fileHandle = open("everybody_codes_e2025_q02_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
a = fileLines[0].split('[')[1].split(']')[0].split(',')
result = (0, 0)
for i in range(0, 3):
	result = mul(result[0], result[1], result[0], result[1])
	result = div(result[0], result[1], 10, 10)
	result = add(result[0], result[1], int(a[0]), int(a[1]))
print("[" + str(result[0]) + "," + str(result[1]) + "]")
