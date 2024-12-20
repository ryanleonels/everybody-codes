#!/usr/bin/python3

runicSymbols = 0
words = []
sentences = []
fileHandle = open("everybody_codes_e2024_q02_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
words = fileLines[0].split(':')[1].split(',')
sentences = fileLines[2:]
nWords = len(words)
nSentences = len(sentences)
for sentence in sentences:
	isRunic = []
	nSentence = len(sentence)
	for i in range(0, nSentence):
		isRunic.append(False)
	for i in range(0, nSentence):
		for j in range(0, nWords):
			if i <= nSentence - len(words[j]):
				if words[j] in sentence[i:i+len(words[j])]:
					for k in range(i, i+len(words[j])):
						isRunic[k] = True
				if words[j][::-1] in sentence[i:i+len(words[j])]:
					for k in range(i, i+len(words[j])):
						isRunic[k] = True
	for i in range(0, nSentence):
		if isRunic[i] == True:
			runicSymbols += 1
print(runicSymbols)