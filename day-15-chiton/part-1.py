import dijkstra 

f = open('input.txt', 'r')

riskLevels = []
for line in f.readlines():
	riskLevels.append(list(map(int, list(line.rstrip()))))

def node(i, j):
	return '(' + str(i) + ',' + str(j) + ')'

graph = dijkstra.Graph()
for i, row in enumerate(riskLevels):
	for j, riskLevel in enumerate(row):
		if i + 1 < len(riskLevels):
			graph.add_edge(node(i, j), node(i + 1, j), riskLevels[i + 1][j])
		if j + 1 < len(row):
			graph.add_edge(node(i, j), node(i, j + 1), riskLevels[i][j + 1])
		if i - 1 > 0:
			graph.add_edge(node(i, j), node(i - 1, j), riskLevels[i - 1][j])
		if j - 1 > 0:
			graph.add_edge(node(i, j), node(i, j - 1), riskLevels[i][j - 1])

dijkstra = dijkstra.DijkstraSPF(graph, node(0, 0))
print(dijkstra.get_distance(node(99, 99)))