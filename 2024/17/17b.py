#!/usr/bin/python3

n = 0
row = 0
col = 0
stars = []
grid = []
starDists = []
fileHandle = open("everybody_codes_e2024_q17_p2.txt", "r")
fileData = fileHandle.read()
fileHandle.close()
fileLines = fileData.split('\n')
i = 0
for fileLine in fileLines:
	if fileLine.strip() == '':
		continue
	grid.append(fileLine)
	n1 = len(fileLine)
	for j in range(0, n1):
		if fileLine[j] == '*':
			stars.append((i, j))
	i += 1
row = len(grid)
col = len(grid[0])
n = len(stars)
#print(stars)
for i in range(0, n):
	starDists.append([])
	for j in range(0, n):
		starDists[i].append(abs(stars[i][0]-stars[j][0])+abs(stars[i][1]-stars[j][1]))
	#print(starDists[i])

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    # print constructed MST stored in parent[]
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    # get total size of constructed MST stored in parent[]
    def getMSTSize(self, parent):
        size = 0
        for i in range(1, self.V):
            size += self.graph[i][parent[i]]
        return size

    # find the vertex with minimum distance value, from the set of vertices not yet included in shortest path tree
    def minKey(self, key, mstSet):
        # Initialize min value
        min = 999999999

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    # construct and print MST for a graph represented using adjacency matrix representation
    def primMST(self):
        # Key values used to pick minimum weight edge in cut
        key = [999999999] * self.V
        parent = [None] * self.V  # Array to store constructed MST

        # Make key 0 so that this vertex is picked as first vertex
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1  # First node is always the root of

        for cout in range(self.V):

            # Pick minimum distance vertex from set of vertices not yet processed (u is always equal to src in first iteration)
            u = self.minKey(key, mstSet)

            # Put minimum distance vertex in shortest path tree
            mstSet[u] = True

            # Update dist value of adjacent vertices of the picked vertex only if the current distance is >= new distance and the vertex is not in the shortest path tree
            for v in range(self.V):
                # graph[u][v] != 0 only for adjacent vertices of m
                # mstSet[v] is false for vertices not yet included in MST
                # Update the key only if graph[u][v] < key[v]
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        #self.printMST(parent)
        return self.getMSTSize(parent)

starGraph = Graph(n)
starGraph.graph = starDists
print(starGraph.primMST()+n)