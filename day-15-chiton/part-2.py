import dijkstra 

f = open('input.txt', 'r')

riskLevels = []
for line in f.readlines():
	riskLevels.append(list(map(int, list(line.rstrip()))))

height = len(riskLevels)
width = len(riskLevels[0])

def riskLevel(i, j):
	return ((riskLevels[i % width][j % height] + int(i / width) + int(j / height) - 1) % 9) + 1

def node(i, j):
	return '(' + str(i) + ',' + str(j) + ')'

graph = dijkstra.Graph()

tiles = 5
for i in range(0, width * tiles):
	for j in range(0, height * tiles):
		graph.add_edge(node(i, j), node(i + 1, j), riskLevel(i + 1, j))
		graph.add_edge(node(i, j), node(i, j + 1), riskLevel(i, j + 1))
		graph.add_edge(node(i, j), node(i - 1, j), riskLevel(i - 1, j))
		graph.add_edge(node(i, j), node(i, j - 1), riskLevel(i, j - 1))

dijkstra = dijkstra.DijkstraSPF(graph, node(0, 0))
print(dijkstra.get_distance(node(width * tiles - 1, height * tiles - 1)))