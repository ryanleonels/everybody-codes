#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q08_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
steps = [int(x) for x in fileData.strip().split(',')]
n = len(steps)
nails = 256
knots = 0
threads = {}
for i in range(0, n - 1):
	thread = (steps[i], steps[i + 1])
	if thread in threads:
		threads[thread] += 1
	else:
		threads[thread] = 1
cutmax = 0
for i in range(1, nails):
	for j in range(i + 1, nails + 1):
		cut = 0
		for thread in threads:
			if thread[0] < thread[1]:
				(a, b) = (thread[0], thread[1])
			else:
				(a, b) = (thread[1], thread[0])
			if i < a and j > a and j < b:
				cut += threads[thread]
			if i > a and i < b and j > b:
				cut += threads[thread]
			if i == a and j == b:
				cut += threads[thread]
		if cut > cutmax:
			print(i, j, cut)
			cutmax = cut
print(cutmax)
