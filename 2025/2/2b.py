#!/usr/bin/python3

import math

def add(x1, y1, x2, y2):
	return (x1 + x2, y1 + y2)

def mul(x1, y1, x2, y2):
	return ((x1 * x2) - (y1 * y2), (x1 * y2) + (y1 * x2))

def div(x1, y1, x2, y2):
	(z1, z2) = (x1 / x2, y1 / y2)
	return (math.floor(z1) if z1 > 0 else math.ceil(z1), math.floor(z2) if z2 > 0 else math.ceil(z2))

fileHandle = open("everybody_codes_e2025_q02_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
a = fileLines[0].split('[')[1].split(']')[0].split(',')
n = 0
for i in range(0, 101):
	line = ''
	for j in range(0, 101):
		p = (int(a[0]) + (i * 10), int(a[1]) + (j * 10))
		r = (0, 0)
		ok = True
		for k in range(0, 100):
			r = mul(r[0], r[1], r[0], r[1])
			r = div(r[0], r[1], 100000, 100000)
			r = add(r[0], r[1], p[0], p[1])
			if r[0] > 1000000 or r[0] < -1000000 or r[1] > 1000000 or r[1] < -1000000:
				ok = False
				break
		if ok:
			n += 1
			line += 'X'
		else:
			line += '.'
	print(line)
print(n)
