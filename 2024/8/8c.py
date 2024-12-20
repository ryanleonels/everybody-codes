#!/usr/bin/python3

fileHandle = open("everybody_codes_e2024_q08_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
n = int(fileData)
nBlocks = 1
nLayers = 1
layers = [1]
nBlocks1 = 202400000000 #202400000000
heights = [1]
while nBlocks < nBlocks1:
	x = ((layers[nLayers-1] * n) % 10) + 10
	layers.append(x)
	n1 = len(heights)
	for i in range(0, n1):
		heights[i] += x
	heights.insert(0, x)
	heights.append(x)
	nBlocks = 0
	n1 = len(heights)
	for i in range(0, n1):
		if i == 0 or i == (n1 - 1):
			removed = 0
		else:
			removed = (n * n1 * heights[i]) % 10
		nBlocks += (heights[i] - removed)
	nLayers += 1
	print((nLayers, nBlocks))
nBlocks -= nBlocks1
print(nBlocks)