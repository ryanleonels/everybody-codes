#!/usr/bin/python3

scales = 0
words = []
sentences = []
fileHandle = open("everybody_codes_e2024_q02_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
words = fileLines[0].split(':')[1].split(',')
sentences = fileLines[2:]
nWords = len(words)
row = len(sentences)
col = len(sentences[0])
isScale = []
for i in range(0, row):
	isScale.append([])
	for j in range(0, col):
		isScale[i].append(False)
for i in range(0, row):
	for j in range(0, col):
		for k in range(0, nWords):
			#left to right
			wordInPos = True
			for l in range(0, len(words[k])):
				x = i
				y = j + l
				if y >= col:
					y -= col
				if sentences[x][y] != words[k][l]:
					wordInPos = False
					break
			if wordInPos == True:
				for l in range(0, len(words[k])):
					x = i
					y = j + l
					if y >= col:
						y -= col
					isScale[x][y] = True
			#right to left
			wordInPos = True
			for l in range(0, len(words[k])):
				x = i
				y = j - l
				if y < 0:
					y += col
				if sentences[x][y] != words[k][l]:
					wordInPos = False
					break
			if wordInPos == True:
				for l in range(0, len(words[k])):
					x = i
					y = j - l
					if y < 0:
						y += col
					isScale[x][y] = True
			#top to bottom
			wordInPos = True
			for l in range(0, len(words[k])):
				x = i + l
				y = j
				if x >= row:
					wordInPos = False
					break
				if sentences[x][y] != words[k][l]:
					wordInPos = False
					break
			if wordInPos == True:
				for l in range(0, len(words[k])):
					x = i + l
					y = j
					isScale[x][y] = True
			#bottom to top
			wordInPos = True
			for l in range(0, len(words[k])):
				x = i - l
				y = j
				if x < 0:
					wordInPos = False
					break
				if sentences[x][y] != words[k][l]:
					wordInPos = False
					break
			if wordInPos == True:
				for l in range(0, len(words[k])):
					x = i - l
					y = j
					isScale[x][y] = True
for i in range(0, row):
	for j in range(0, col):
		if isScale[i][j] == True:
			scales += 1
print(scales)
