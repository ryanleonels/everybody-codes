#!/usr/local/bin/python3

from heapq import heapify, heappop, heappush

startAlt = 10000
altDiff = 100
minAlt = startAlt - altDiff
maxAlt = startAlt + altDiff
start = (-1, -1, 'v', startAlt)
s = (-1, -1)
a = (-1, -1)
b = (-1, -1)
c = (-1, -1)
grid = []
adj = {}
fileHandle = open("everybody_codes_e2024_q20_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
row = len(grid)
col = len(grid[0])
for i in range(0, row):
	for j in range(0, col):
		if grid[i][j] != '#':
			for alt in range(minAlt, maxAlt + 1):
				adj[(i, j, 'v', alt)] = {}
				adj[(i, j, '^', alt)] = {}
				adj[(i, j, '>', alt)] = {}
				adj[(i, j, '<', alt)] = {}
				if i > 0 and grid[i - 1][j] != '#':
					alt1 = alt
					match grid[i - 1][j]:
						case '.':
							alt1 = alt - 1
						case '-':
							alt1 = alt - 2
						case '+':
							alt1 = alt + 1
						case 'A':
							alt1 = alt - 1
						case 'B':
							alt1 = alt - 1
						case 'C':
							alt1 = alt - 1
						case 'S':
							alt1 = alt - 1
					if alt1 >= minAlt and alt1 <= maxAlt:
						adj[(i, j, '^', alt)][(i - 1, j, '^', alt1)] = 1
						adj[(i, j, '<', alt)][(i - 1, j, '^', alt1)] = 1
						adj[(i, j, '>', alt)][(i - 1, j, '^', alt1)] = 1
				if i < row - 1 and grid[i + 1][j] != '#':
					alt1 = alt
					match grid[i + 1][j]:
						case '.':
							alt1 = alt - 1
						case '-':
							alt1 = alt - 2
						case '+':
							alt1 = alt + 1
						case 'A':
							alt1 = alt - 1
						case 'B':
							alt1 = alt - 1
						case 'C':
							alt1 = alt - 1
						case 'S':
							alt1 = alt - 1
					if alt1 >= minAlt and alt1 <= maxAlt:
						adj[(i, j, 'v', alt)][(i + 1, j, 'v', alt1)] = 1
						adj[(i, j, '<', alt)][(i + 1, j, 'v', alt1)] = 1
						adj[(i, j, '>', alt)][(i + 1, j, 'v', alt1)] = 1
				if j > 0 and grid[i][j - 1] != '#':
					alt1 = alt
					match grid[i][j - 1]:
						case '.':
							alt1 = alt - 1
						case '-':
							alt1 = alt - 2
						case '+':
							alt1 = alt + 1
						case 'A':
							alt1 = alt - 1
						case 'B':
							alt1 = alt - 1
						case 'C':
							alt1 = alt - 1
						case 'S':
							alt1 = alt - 1
					if alt1 >= minAlt and alt1 <= maxAlt:
						adj[(i, j, '^', alt)][(i, j - 1, '<', alt1)] = 1
						adj[(i, j, 'v', alt)][(i, j - 1, '<', alt1)] = 1
						adj[(i, j, '<', alt)][(i, j - 1, '<', alt1)] = 1
				if j < col - 1 and grid[i][j + 1] != '#':
					alt1 = alt
					match grid[i][j + 1]:
						case '.':
							alt1 = alt - 1
						case '-':
							alt1 = alt - 2
						case '+':
							alt1 = alt + 1
						case 'A':
							alt1 = alt - 1
						case 'B':
							alt1 = alt - 1
						case 'C':
							alt1 = alt - 1
						case 'S':
							alt1 = alt - 1
					if alt1 >= minAlt and alt1 <= maxAlt:
						adj[(i, j, '^', alt)][(i, j + 1, '>', alt1)] = 1
						adj[(i, j, 'v', alt)][(i, j + 1, '>', alt1)] = 1
						adj[(i, j, '>', alt)][(i, j + 1, '>', alt1)] = 1
		if grid[i][j] == 'S':
			start = (i, j, 'v', startAlt)
			s = (i, j)
		if grid[i][j] == 'A':
			a = (i, j)
		if grid[i][j] == 'B':
			b = (i, j)
		if grid[i][j] == 'C':
			c = (i, j)

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

adjGraph = Graph(adj)
maxDist = 0
print('start')
distances = adjGraph.shortest_distances(start)

da1 = {}
da2 = {}
da3 = {}
da4 = {}
for i in range(minAlt, maxAlt + 1):
	node1 = (a[0], a[1], '^', i)
	node2 = (a[0], a[1], 'v', i)
	node3 = (a[0], a[1], '>', i)
	node4 = (a[0], a[1], '<', i)
	da1[i] = distances[node1]
	da2[i] = distances[node2]
	da3[i] = distances[node3]
	da4[i] = distances[node4]
print(da1)
print(da2)
print(da3)
print(da4)

a1 = (a[0], a[1], '^', startAlt)
a2 = (a[0], a[1], 'v', startAlt)
a3 = (a[0], a[1], '>', startAlt)
a4 = (a[0], a[1], '<', startAlt)
print('a1')
distances_a1 = adjGraph.shortest_distances(a1)
print('a2')
distances_a2 = adjGraph.shortest_distances(a2)
print('a3')
distances_a3 = adjGraph.shortest_distances(a3)
print('a4')
distances_a4 = adjGraph.shortest_distances(a4)

db1 = {}
db2 = {}
db3 = {}
db4 = {}
for i in range(minAlt, maxAlt + 1): # alt when reaching b
	# b1[10000] = min(a1/2/3/4[10000]+a1/2/3/4b1[10000],a1/2/3/4[10001]+a1/2/3/4b1[9999],a1/2/3/4[10002]+a1/2/3/4b1[9998], etc.)
	minb1 = float("inf")
	minb2 = float("inf")
	minb3 = float("inf")
	minb4 = float("inf")
	for j in range(minAlt, maxAlt + 1): # previous alt when reaching a
		neededAlt = startAlt + (i - j)
		if neededAlt >= minAlt and neededAlt <= maxAlt:
			node1 = (b[0], b[1], '^', neededAlt)
			node2 = (b[0], b[1], 'v', neededAlt)
			node3 = (b[0], b[1], '>', neededAlt)
			node4 = (b[0], b[1], '<', neededAlt)
			curb1 = da1[j] + distances_a1[node1]
			if curb1 < minb1:
				minb1 = curb1
			curb1 = da2[j] + distances_a2[node1]
			if curb1 < minb1:
				minb1 = curb1
			curb1 = da3[j] + distances_a3[node1]
			if curb1 < minb1:
				minb1 = curb1
			curb1 = da4[j] + distances_a4[node1]
			if curb1 < minb1:
				minb1 = curb1
			curb2 = da1[j] + distances_a1[node2]
			if curb2 < minb2:
				minb2 = curb2
			curb2 = da2[j] + distances_a2[node2]
			if curb2 < minb2:
				minb2 = curb2
			curb2 = da3[j] + distances_a3[node2]
			if curb2 < minb2:
				minb2 = curb2
			curb2 = da4[j] + distances_a4[node2]
			if curb2 < minb2:
				minb2 = curb2
			curb3 = da1[j] + distances_a1[node3]
			if curb3 < minb3:
				minb3 = curb3
			curb3 = da2[j] + distances_a2[node3]
			if curb3 < minb3:
				minb3 = curb3
			curb3 = da3[j] + distances_a3[node3]
			if curb3 < minb3:
				minb3 = curb3
			curb3 = da4[j] + distances_a4[node3]
			if curb3 < minb3:
				minb3 = curb3
			curb4 = da1[j] + distances_a1[node4]
			if curb4 < minb4:
				minb4 = curb4
			curb4 = da2[j] + distances_a2[node4]
			if curb4 < minb4:
				minb4 = curb4
			curb4 = da3[j] + distances_a3[node4]
			if curb4 < minb4:
				minb4 = curb4
			curb4 = da4[j] + distances_a4[node4]
			if curb4 < minb4:
				minb4 = curb4
	db1[i] = minb1
	db2[i] = minb2
	db3[i] = minb3
	db4[i] = minb4
print(db1)
print(db2)
print(db3)
print(db4)

b1 = (b[0], b[1], '^', startAlt)
b2 = (b[0], b[1], 'v', startAlt)
b3 = (b[0], b[1], '>', startAlt)
b4 = (b[0], b[1], '<', startAlt)
print('b1')
distances_b1 = adjGraph.shortest_distances(b1)
print('b2')
distances_b2 = adjGraph.shortest_distances(b2)
print('b3')
distances_b3 = adjGraph.shortest_distances(b3)
print('b4')
distances_b4 = adjGraph.shortest_distances(b4)

dc1 = {}
dc2 = {}
dc3 = {}
dc4 = {}
for i in range(minAlt, maxAlt + 1): # alt when reaching c
	minc1 = float("inf")
	minc2 = float("inf")
	minc3 = float("inf")
	minc4 = float("inf")
	for j in range(minAlt, maxAlt + 1): # previous alt when reaching b
		neededAlt = startAlt + (i - j)
		if neededAlt >= minAlt and neededAlt <= maxAlt:
			node1 = (c[0], c[1], '^', neededAlt)
			node2 = (c[0], c[1], 'v', neededAlt)
			node3 = (c[0], c[1], '>', neededAlt)
			node4 = (c[0], c[1], '<', neededAlt)
			curc1 = db1[j] + distances_b1[node1]
			if curc1 < minc1:
				minc1 = curc1
			curc1 = db2[j] + distances_b2[node1]
			if curc1 < minc1:
				minc1 = curc1
			curc1 = db3[j] + distances_b3[node1]
			if curc1 < minc1:
				minc1 = curc1
			curc1 = db4[j] + distances_b4[node1]
			if curc1 < minc1:
				minc1 = curc1
			curc2 = db1[j] + distances_b1[node2]
			if curc2 < minc2:
				minc2 = curc2
			curc2 = db2[j] + distances_b2[node2]
			if curc2 < minc2:
				minc2 = curc2
			curc2 = db3[j] + distances_b3[node2]
			if curc2 < minc2:
				minc2 = curc2
			curc2 = db4[j] + distances_b4[node2]
			if curc2 < minc2:
				minc2 = curc2
			curc3 = db1[j] + distances_b1[node3]
			if curc3 < minc3:
				minc3 = curc3
			curc3 = db2[j] + distances_b2[node3]
			if curc3 < minc3:
				minc3 = curc3
			curc3 = db3[j] + distances_b3[node3]
			if curc3 < minc3:
				minc3 = curc3
			curc3 = db4[j] + distances_b4[node3]
			if curc3 < minc3:
				minc3 = curc3
			curc4 = db1[j] + distances_b1[node4]
			if curc4 < minc4:
				minc4 = curc4
			curc4 = db2[j] + distances_b2[node4]
			if curc4 < minc4:
				minc4 = curc4
			curc4 = db3[j] + distances_b3[node4]
			if curc4 < minc4:
				minc4 = curc4
			curc4 = db4[j] + distances_b4[node4]
			if curc4 < minc4:
				minc4 = curc4
	dc1[i] = minc1
	dc2[i] = minc2
	dc3[i] = minc3
	dc4[i] = minc4
print(dc1)
print(dc2)
print(dc3)
print(dc4)

c1 = (c[0], c[1], '^', startAlt)
c2 = (c[0], c[1], 'v', startAlt)
c3 = (c[0], c[1], '>', startAlt)
c4 = (c[0], c[1], '<', startAlt)
print('c1')
distances_c1 = adjGraph.shortest_distances(c1)
print('c2')
distances_c2 = adjGraph.shortest_distances(c2)
print('c3')
distances_c3 = adjGraph.shortest_distances(c3)
print('c4')
distances_c4 = adjGraph.shortest_distances(c4)

ds = {}
shortestTime = float("inf")
for i in range(startAlt, maxAlt + 1): # alt when reaching s
	mins = float("inf")
	for j in range(minAlt, maxAlt + 1): # previous alt when reaching c
		neededAlt = startAlt + (i - j)
		if neededAlt >= minAlt and neededAlt <= maxAlt:
			node = (s[0], s[1], '^', neededAlt)
			curs = dc1[j] + distances_c1[node]
			if curs < mins:
				mins = curs
			curs = dc2[j] + distances_c2[node]
			if curs < mins:
				mins = curs
			curs = dc3[j] + distances_c3[node]
			if curs < mins:
				mins = curs
			curs = dc4[j] + distances_c4[node]
			if curs < mins:
				mins = curs
	ds[i] = mins
	if mins < shortestTime:
		shortestTime = mins
print(ds)
print(shortestTime)