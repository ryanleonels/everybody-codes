#!/usr/bin/python3

fileHandle = open("everybody_codes_e2025_q07_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
names = fileLines[0].strip().split(',')
rules = {}
allnames = {}
for i in range(2, len(fileLines)):
	if fileLines[i].strip() == '':
		continue
	before = fileLines[i].split(' > ')[0]
	after = fileLines[i].split(' > ')[1].strip().split(',')
	rules[before] = after
for i in range(0, len(names)):
	ok = True
	for j in range(0, len(names[i]) - 1):
		if names[i][j] in rules and names[i][j + 1] not in rules[names[i][j]]:
			ok = False
			break
	if ok:
		if len(names[i]) not in allnames:
			allnames[len(names[i])] = set()
		allnames[len(names[i])].add(names[i])
for i in range(1, 11):
	if i + 1 not in allnames:
		allnames[i + 1] = set()
	if i in allnames:
		for name in allnames[i]:
			if name[i - 1] in rules:
				for ch in rules[name[i - 1]]:
					allnames[i + 1].add(name + ch)
	#print(i + 1, len(allnames[i + 1]))
total = 0
for i in range(7, 12):
	total += len(allnames[i])
print(total)
