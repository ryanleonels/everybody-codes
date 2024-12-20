#!/usr/local/bin/python3

from heapq import heapify, heappop, heappush

startAlt = 384400
altDiff = 100
minAlt = startAlt - altDiff
maxAlt = startAlt + altDiff
repeats = 3 # repeats until pattern is fully established (at least 2-3 as the pattern starts repeating at 1-2)
start = (-1, -1, 'v', startAlt)
grid = []
adj = {}
fileHandle = open("everybody_codes_e2024_q20_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
row1 = len(grid)
col = len(grid[0])
for i in range(0, repeats):
	for fileLine in fileLines:
		if fileLine.strip() == '':
			continue
		grid.append(fileLine.replace('S', '.'))
row = len(grid)
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
						case 'S':
							alt1 = alt - 1
					if alt1 >= minAlt and alt1 <= maxAlt:
						adj[(i, j, '^', alt)][(i, j + 1, '>', alt1)] = 1
						adj[(i, j, 'v', alt)][(i, j + 1, '>', alt1)] = 1
						adj[(i, j, '>', alt)][(i, j + 1, '>', alt1)] = 1
		if grid[i][j] == 'S':
			start = (i, j, 'v', startAlt)
			s = (i, j)

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
distances = adjGraph.shortest_distances(start)
maxAltitudes = {}
for i in range(0, row):
	if i % row1 == 0:
		print("repeat " + str(i // row1))
	maxAltitude = 0
	for j in range(0, col):
		for k in range(maxAlt, minAlt - 1, -1):
			node1 = (i, j, '^', k)
			node2 = (i, j, 'v', k)
			node3 = (i, j, '>', k)
			node4 = (i, j, '<', k)
			if node1 in distances and distances[node1] != float("inf"):
				if k > maxAltitude:
					maxAltitude = k
				break
			if node2 in distances and distances[node2] != float("inf"):
				if k > maxAltitude:
					maxAltitude = k
				break
			if node3 in distances and distances[node3] != float("inf"):
				if k > maxAltitude:
					maxAltitude = k
				break
			if node4 in distances and distances[node4] != float("inf"):
				if k > maxAltitude:
					maxAltitude = k
				break
	print([i, maxAltitude])
	maxAltitudes[i] = maxAltitude

print("repeat length: " + str(row1))
dropPerRepeat = maxAltitudes[row1 * (repeats - 1)] - maxAltitudes[row1 * repeats]
print("altitude drop per repeat: " + str(dropPerRepeat))
minAlt = startAlt
for i in range(row1 * repeats, row1 * (repeats + 1)):
	if maxAltitudes[i] < minAlt:
		minAlt = maxAltitudes[i]
print("minimum altitude at repeat " + str(repeats) + ": " + str(minAlt))
repeatsTo0 = (minAlt + (dropPerRepeat - 1)) // dropPerRepeat #maxAltitudes[row1 * repeats] // dropPerRepeat
print(str(repeatsTo0) + " more repeat(s) needed to reach altitude 0")
print("repeat " + str(repeats + repeatsTo0))
for i in range(0, row1):
	i1 = ((repeats + repeatsTo0) * row1) + i
	altitude = maxAltitudes[(row1 * repeats) + i] - (repeatsTo0 * dropPerRepeat)
	print([i1, altitude])
	if altitude <= 0:
		break
print("altitude 0 first reached at " + str(i1))