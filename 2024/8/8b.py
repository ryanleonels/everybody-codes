#!/usr/bin/python3

fileHandle = open("everybody_codes_e2024_q08_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
n = int(fileData)
nBlocks = 1
nLayers = 1
layers = [1]
while nBlocks < 20240000:
	x = (layers[nLayers-1] * n) % 1111
	layers.append(x)
	nBlocks += (((2 * nLayers) + 1) * layers[nLayers])
	nLayers += 1
nBlocks -= 20240000
width = (nLayers * 2) - 1
result = nBlocks * width
print(result)