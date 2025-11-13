#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q08_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
steps = [int(x) for x in fileData.strip().split(',')]
n = len(steps)
nails = 256
knots = 0
threads = set()
for i in range(0, n - 1):
	thread = (steps[i], steps[i + 1])
	if thread[0] < thread[1]:
		(a, b) = (thread[0], thread[1])
	else:
		(a, b) = (thread[1], thread[0])
	knots1 = 0
	for thread1 in threads:
		if thread1[0] < thread1[1]:
			(a1, b1) = (thread1[0], thread1[1])
		else:
			(a1, b1) = (thread1[1], thread1[0])
		if a < a1 and b > a1 and b < b1:
			knots1 += 1
		if a > a1 and a < b1 and b > b1:
			knots1 += 1
	threads.add(thread)
	knots += knots1
print(knots)
