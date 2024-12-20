#!/usr/bin/python3

from heapq import heapify, heappop, heappush

start = (-1, -1)
herbs = []
grid = []
adj = {}
fileHandle = open("everybody_codes_e2024_q15_p1.txt", "r")
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
		if grid[i][j] == '.':
			if i == 0:
				start = (i, j)
			adj[(i, j)] = {}
			if i > 0 and grid[i - 1][j] != '#':
				adj[(i, j)][(i - 1, j)] = 1
			if i < row - 1 and grid[i + 1][j] != '#':
				adj[(i, j)][(i + 1, j)] = 1
			if j > 0 and grid[i][j - 1] != '#':
				adj[(i, j)][(i, j - 1)] = 1
			if j < col - 1 and grid[i][j + 1] != '#':
				adj[(i, j)][(i, j + 1)] = 1
		if grid[i][j] == 'H':
			herbs.append((i, j))
			adj[(i, j)] = {}

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
minDist = 999999999

distances = adjGraph.shortest_distances(start)
for herb in herbs:
	if distances[herb] < minDist:
		minDist = distances[herb]

print(minDist * 2)