#!/usr/bin/python3

runicWords = 0
words = []
sentence = []
fileHandle = open("everybody_codes_e2024_q02_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
words = fileLines[0].split(':')[1].split(',')
sentence = fileLines[2].split(' ')
nWords = len(words)
nSentence = len(sentence)
for i in range(0, nSentence):
	for j in range(0, nWords):
		if words[j] in sentence[i]:
			runicWords += 1
print(runicWords)