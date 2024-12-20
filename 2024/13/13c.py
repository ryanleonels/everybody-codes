#!/usr/bin/python3

from heapq import heapify, heappop, heappush

def level(ch):
	if ch == 'S' or ch == 'E':
		return 0
	return int(ch)

grid = []
adj = {}
nodesStart = []
nodeEnd = (-1, -1)
fileHandle = open("everybody_codes_e2024_q13_p3.txt", "r")
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
		if grid[i][j] == 'S':
			nodesStart.append((i, j))
		if grid[i][j] == 'E':
			nodeEnd = (i, j)
		if grid[i][j] != ' ' and grid[i][j] != '#':
			adj[(i, j)] = {}
			if grid[i][j] == 'E':
				continue
			curLevel = level(grid[i][j])
			if i > 0 and grid[i-1][j] != ' ' and grid[i-1][j] != '#':
				level1 = level(grid[i-1][j])
				diff = abs(curLevel - level1)
				if diff > 5:
					diff = 10 - diff
				adj[(i, j)][(i-1, j)] = diff + 1
			if i < row-1 and grid[i+1][j] != ' ' and grid[i+1][j] != '#':
				level1 = level(grid[i+1][j])
				diff = abs(curLevel - level1)
				if diff > 5:
					diff = 10 - diff
				adj[(i, j)][(i+1, j)] = diff + 1
			if j > 0 and grid[i][j-1] != ' ' and grid[i][j-1] != '#':
				level1 = level(grid[i][j-1])
				diff = abs(curLevel - level1)
				if diff > 5:
					diff = 10 - diff
				adj[(i, j)][(i, j-1)] = diff + 1
			if j < col-1 and grid[i][j+1] != ' ' and grid[i][j+1] != '#':
				level1 = level(grid[i][j+1])
				diff = abs(curLevel - level1)
				if diff > 5:
					diff = 10 - diff
				adj[(i, j)][(i, j+1)] = diff + 1
#for node in adj:
	#print([node, adj[node]])

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
bestTime = 999999999

for nodeStart in nodesStart:
	distances = adjGraph.shortest_distances(nodeStart)
	#print(distances, "\n")

	curTime = distances[nodeEnd]
	print({nodeStart: curTime})

	if curTime < bestTime:
		bestTime = curTime

print(bestTime)