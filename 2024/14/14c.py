#!/usr/bin/python3

from heapq import heapify, heappop, heappush

mainTrunk = 0
leaves = set()
segments = set()
adj = {}
fileHandle = open("everybody_codes_e2024_q14_p3.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	trunk = int(fileLine[1:].split(',')[0])
	if trunk > mainTrunk:
		mainTrunk = trunk
	steps = fileLine.split(',')
	segment = (0, 0, 0)
	for step in steps:
		direction = step[0]
		num = int(step[1:])
		if direction == 'U':
			for i in range(0, num):
				segment = (segment[0] + 1, segment[1], segment[2])
				segments.add(segment)
		if direction == 'D':
			for i in range(0, num):
				segment = (segment[0] - 1, segment[1], segment[2])
				segments.add(segment)
		if direction == 'R':
			for i in range(0, num):
				segment = (segment[0], segment[1] + 1, segment[2])
				segments.add(segment)
		if direction == 'L':
			for i in range(0, num):
				segment = (segment[0], segment[1] - 1, segment[2])
				segments.add(segment)
		if direction == 'F':
			for i in range(0, num):
				segment = (segment[0], segment[1], segment[2] + 1)
				segments.add(segment)
		if direction == 'B':
			for i in range(0, num):
				segment = (segment[0], segment[1], segment[2] - 1)
				segments.add(segment)
	leaves.add(segment)
#print(len(segments))
#print(leaves)
#print(mainTrunk)
for segment in segments:
	adj[segment] = {}
	if segment not in leaves:
		(x, y, z) = segment
		if (x - 1, y, z) in segments:
			adj[segment][(x - 1, y, z)] = 1
		if (x + 1, y, z) in segments:
			adj[segment][(x + 1, y, z)] = 1
		if (x, y - 1, z) in segments:
			adj[segment][(x, y - 1, z)] = 1
		if (x, y + 1, z) in segments:
			adj[segment][(x, y + 1, z)] = 1
		if (x, y, z - 1) in segments:
			adj[segment][(x, y, z - 1)] = 1
		if (x, y, z + 1) in segments:
			adj[segment][(x, y, z + 1)] = 1

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
minMurkiness = 999999999

for i in range(1, mainTrunk + 1):
	nodeStart = (i, 0, 0)
	distances = adjGraph.shortest_distances(nodeStart)
	#print(distances, "\n")

	#x = []
	murkiness = 0
	for leaf in leaves:
		dist = distances[leaf]
		#x.append(dist)
		murkiness += dist
	#print((i, x))
	#print(murkiness)

	if murkiness < minMurkiness:
		minMurkiness = murkiness

print(minMurkiness)
