#!/usr/bin/python3

fileHandle = open("everybody_codes_e2024_q08_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
n = int(fileData)
n2 = int(n ** 0.5)
if n2 * n2 < n:
	n2 += 1
blocks = (n2 * n2) - n
width = (n2 * 2) - 1
result = blocks * width
print(result)