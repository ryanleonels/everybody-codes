#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q07_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
names = fileLines[0].strip().split(',')
rules = {}
for i in range(2, len(fileLines)):
	if fileLines[i].strip() == '':
		continue
	before = fileLines[i].split(' > ')[0]
	after = fileLines[i].split(' > ')[1].strip().split(',')
	rules[before] = after
for i in range(0, len(names)):
	ok = True
	for j in range(0, len(names[i]) - 1):
		if names[i][j] in rules:
			if names[i][j + 1] not in rules[names[i][j]]:
				ok = False
				break
	if ok:
		print(names[i])
