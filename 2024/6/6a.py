#!/usr/bin/python3

branches = {}
nodes = {}
fileHandle = open("everybody_codes_e2024_q06_p1.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	branches[fileLine.split(':')[0]] = fileLine.split(':')[1].split(',')
nodes['RR'] = {'length': 0, 'prev': '', 'done': False}
done = False
fruits = {}
while done == False:
	n = 0
	nodes1 = {}
	for node in nodes:
		if nodes[node]['done'] == False and node in branches:
			for branch in branches[node]:
				if branch == '@':
					length = nodes[node]['length']
					if length in fruits:
						fruits[length].append(node)
					else:
						fruits[length] = [node]
				else:
					nodes1[branch] = {'length': nodes[node]['length'] + 1, 'prev': node, 'done': False}
			nodes[node]['done'] = True
			n += 1
	for node in nodes1:
		nodes[node] = nodes1[node]
	if n == 0:
		done = True
mostPowerfulNode = ''
for len1 in fruits:
	if len(fruits[len1]) == 1:
		mostPowerfulNode = fruits[len1][0]
path = "@"
node = mostPowerfulNode
while node != '':
	path = node + path
	node = nodes[node]['prev']
print(path)