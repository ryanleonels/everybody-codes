#!/usr/bin/python3

from heapq import heapify, heappop, heappush

startL = (-1, -1)
start = (-1, -1)
startR = (-1, -1)
herbsL = {}
herbs = {}
herbsR = {}
grid = []
adjL = {}
adj = {}
adjR = {}
fileHandle = open("everybody_codes_e2024_q15_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(list(fileLine))
row = len(grid)
col = len(grid[0])
col3 = col // 3

for i in range(0, row):
	if grid[i][col3 - 1] != '#':
		grid[i][col3 - 1] = '#'
	if grid[i][col3] != '#':
		grid[i][col3] = '#'
	if grid[i][col3 * 2- 1] != '#':
		grid[i][col3 * 2 - 1] = '#'
	if grid[i][col3 * 2] != '#':
		grid[i][col3 * 2] = '#'
if grid[row - 2][1] == 'E':
	grid[row - 2][1] = '.'
if grid[row - 2][col3 * 2 - 2] == 'K':
	grid[row - 2][col3 * 2 - 2] = 'L'
if grid[row - 2][col - 2] == 'R':
	grid[row - 2][col - 2] = '.'

"""for i in range(0, row):
	print(''.join(grid[i][:col3]))
print()
for i in range(0, row):
	print(''.join(grid[i][col3:col3*2]))
print()
for i in range(0, row):
	print(''.join(grid[i][col3*2:]))"""

for i in range(0, row):
	for j in range(0, col3):
		if grid[i][j] == '.' or (grid[i][j] >= 'A' and grid[i][j] <= 'Z'):
			if grid[i][j] == 'E':
				startL = (i, j)
			adjL[(i, j)] = {}
			if i > 0 and grid[i - 1][j] != '#' and grid[i - 1][j] != '~':
				adjL[(i, j)][(i - 1, j)] = 1
			if i < row - 1 and grid[i + 1][j] != '#' and grid[i + 1][j] != '~':
				adjL[(i, j)][(i + 1, j)] = 1
			if j > 0 and grid[i][j - 1] != '#' and grid[i][j - 1] != '~':
				adjL[(i, j)][(i, j - 1)] = 1
			if j < col3 - 1 and grid[i][j + 1] != '#' and grid[i][j + 1] != '~':
				adjL[(i, j)][(i, j + 1)] = 1
		if grid[i][j] >= 'A' and grid[i][j] <= 'Z' and grid[i][j] != 'E':
			herbsL[(i, j)] = grid[i][j]
for i in range(0, row):
	for j in range(col3, col3 * 2):
		if grid[i][j] == '.' or (grid[i][j] >= 'A' and grid[i][j] <= 'Z'):
			if i == 0:
				start = (i, j)
			adj[(i, j)] = {}
			if i > 0 and grid[i - 1][j] != '#' and grid[i - 1][j] != '~':
				adj[(i, j)][(i - 1, j)] = 1
			if i < row - 1 and grid[i + 1][j] != '#' and grid[i + 1][j] != '~':
				adj[(i, j)][(i + 1, j)] = 1
			if j > col3 and grid[i][j - 1] != '#' and grid[i][j - 1] != '~':
				adj[(i, j)][(i, j - 1)] = 1
			if j < col3 * 2 - 1 and grid[i][j + 1] != '#' and grid[i][j + 1] != '~':
				adj[(i, j)][(i, j + 1)] = 1
		if grid[i][j] >= 'A' and grid[i][j] <= 'Z':
			herbs[(i, j)] = grid[i][j]
for i in range(0, row):
	for j in range(col3 * 2, col3 * 3):
		if grid[i][j] == '.' or (grid[i][j] >= 'A' and grid[i][j] <= 'Z'):
			if grid[i][j] == 'R':
				startR = (i, j)
			adjR[(i, j)] = {}
			if i > 0 and grid[i - 1][j] != '#' and grid[i - 1][j] != '~':
				adjR[(i, j)][(i - 1, j)] = 1
			if i < row - 1 and grid[i + 1][j] != '#' and grid[i + 1][j] != '~':
				adjR[(i, j)][(i + 1, j)] = 1
			if j > col3 * 2 and grid[i][j - 1] != '#' and grid[i][j - 1] != '~':
				adjR[(i, j)][(i, j - 1)] = 1
			if j < col3 * 3 - 1 and grid[i][j + 1] != '#' and grid[i][j + 1] != '~':
				adjR[(i, j)][(i, j + 1)] = 1
		if grid[i][j] >= 'A' and grid[i][j] <= 'Z' and grid[i][j] != 'R':
			herbsR[(i, j)] = grid[i][j]

class Graph:
	def __init__(self, graph: dict = {}):
		self.graph = graph  # A dictionary for the adjacency list

	def add_edge(self, node1, node2, weight):
		if node1 not in self.graph:  # Check if the node is already added
			self.graph[node1] = {}  # If not, create the node
		self.graph[node1][node2] = weight  # Else, add a connection to its neighbor

	def shortest_distances(self, source: str):
		# Initialize the values of all nodes with infinity
		distances = {node: float("inf") for node in self.graph}
		distances[source] = 0  # Set the source value to 0

		# Initialize a priority queue
		pq = [(0, source)]
		heapify(pq)

		# Create a set to hold visited nodes
		visited = set()

		while pq:  # While the priority queue isn't empty
			current_distance, current_node = heappop(pq) # Get the node with the min distance

			if current_node in visited:
			   continue  # Skip already visited nodes
			visited.add(current_node)  # Else, add the node to visited set

			for neighbor, weight in self.graph[current_node].items():
				# Calculate the distance from current_node to the neighbor
				tentative_distance = current_distance + weight
				if tentative_distance < distances[neighbor]:
					distances[neighbor] = tentative_distance
					heappush(pq, (tentative_distance, neighbor))

		return distances

adjGraphL = Graph(adjL)
adjGraph = Graph(adj)
adjGraphR = Graph(adjR)
minDistL = 999999999
minDist = 999999999
minDistR = 999999999

distancesL = adjGraphL.shortest_distances(startL)
distances = adjGraph.shortest_distances(start)
distancesR = adjGraphR.shortest_distances(startR)
herbDistancesL = {}
herbDistances = {}
herbDistancesR = {}
for herb in herbsL:
	herbDistancesL[herb] = adjGraphL.shortest_distances(herb)
for herb in herbs:
	herbDistances[herb] = adjGraph.shortest_distances(herb)
for herb in herbsR:
	herbDistancesR[herb] = adjGraphR.shortest_distances(herb)

distTableL = {}
distTableL[startL] = {}
for herb in herbsL:
	distTableL[startL][herb] = distancesL[herb]
for herb1 in herbsL:
	distTableL[herb1] = {}
	distTableL[herb1][startL] = herbDistancesL[herb1][startL]
	for herb2 in herbsL:
		distTableL[herb1][herb2] = herbDistancesL[herb1][herb2]

distTable = {}
distTable[start] = {}
for herb in herbs:
	distTable[start][herb] = distances[herb]
for herb1 in herbs:
	distTable[herb1] = {}
	distTable[herb1][start] = herbDistances[herb1][start]
	for herb2 in herbs:
		distTable[herb1][herb2] = herbDistances[herb1][herb2]

distTableR = {}
distTableR[startR] = {}
for herb in herbsR:
	distTableR[startR][herb] = distancesR[herb]
for herb1 in herbsR:
	distTableR[herb1] = {}
	distTableR[herb1][startR] = herbDistancesR[herb1][startR]
	for herb2 in herbsR:
		distTableR[herb1][herb2] = herbDistancesR[herb1][herb2]

herbTypesL = set()
for herb in herbsL:
	herbTypesL.add(herbsL[herb])
herbTypes = set()
for herb in herbs:
	herbTypes.add(herbs[herb])
herbTypesR = set()
for herb in herbsR:
	herbTypesR.add(herbsR[herb])

"""for herbType in sorted(herbTypesL):
	n = 0
	for herb in herbsL:
		if herbsL[herb] == herbType:
			n += 1
	print((herbType, n))
print()
for herbType in sorted(herbTypes):
	n = 0
	for herb in herbs:
		if herbs[herb] == herbType:
			n += 1
	print((herbType, n))
print()
for herbType in sorted(herbTypesR):
	n = 0
	for herb in herbsR:
		if herbsR[herb] == herbType:
			n += 1
	print((herbType, n))"""

"""
('A', 32)
('B', 52)
('C', 32)
('D', 1)
('E', 2)
('G', 32)
('H', 52)
('I', 32)
('J', 1)
('K', 2)
('N', 32)
('O', 52)
('P', 32)
('Q', 1)
('R', 2)
left: ABCDE (right E)
mid: EGHIJKR (right E / left R) K1 / K2, replace K2 with L?
right: NOPQR (left R)
"""

x = 0

def getDistL(curNode, curDist, typesToGet):
	global x
	x += 1
	if x % 100000 == 0:
		print(x)
	if len(typesToGet) == 0:
		return curDist + distTableL[curNode][startL]
	distMin = 999999999
	for herb in herbsL:
		herbType = herbsL[herb]
		if herbType in typesToGet:
			type1 = typesToGet.copy()
			type1.remove(herbType)
			dist = getDistL(herb, curDist + distTableL[curNode][herb], type1)
			if dist < distMin:
				distMin = dist
	return distMin

minDistL = getDistL(startL, 0, herbTypesL)
print(minDistL)

x = 0

def getDistR(curNode, curDist, typesToGet):
	global x
	x += 1
	if x % 100000 == 0:
		print(x)
	if len(typesToGet) == 0:
		return curDist + distTableR[curNode][startR]
	distMin = 999999999
	for herb in herbsR:
		herbType = herbsR[herb]
		if herbType in typesToGet:
			type1 = typesToGet.copy()
			type1.remove(herbType)
			dist = getDistR(herb, curDist + distTableR[curNode][herb], type1)
			if dist < distMin:
				distMin = dist
	return distMin

minDistR = getDistR(startR, 0, herbTypesR)
print(minDistR)

x = 0

def getDist(curNode, curDist, typesToGet):
	global x
	x += 1
	if x % 100000 == 0:
		print(x)
	if len(typesToGet) == 0:
		return curDist + distTable[curNode][start]
	distMin = 999999999
	for herb in herbs:
		herbType = herbs[herb]
		if herbType in typesToGet:
			type1 = typesToGet.copy()
			type1.remove(herbType)
			dist = getDist(herb, curDist + distTable[curNode][herb], type1)
			if dist < distMin:
				distMin = dist
	return distMin

minDist = getDist(start, 0, herbTypes)
print(minDist)

minDistTotal = minDistL + minDist + minDistR + 12
print(minDistTotal)
