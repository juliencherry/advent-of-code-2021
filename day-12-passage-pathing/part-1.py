from collections import defaultdict
from collections import deque

f = open('input.txt', 'r')

caveEdges = defaultdict(lambda: [])

for line in f.readlines():
	startCave, endCave = line.split('-')
	caveEdges[startCave].append(endCave.rstrip())
	caveEdges[endCave.rstrip()].append(startCave)

def paths(startingPath, smallCavesVisited):
	lastCave = startingPath[-1]
	nextCaves = caveEdges[lastCave]
	
	if lastCave == 'end':
		return [list(startingPath)]
	
	allPaths = []
	for nextCave in nextCaves:
		if nextCave in smallCavesVisited:
			continue

		newSmallCavesVisited = smallCavesVisited.copy()
		if nextCave == nextCave.lower():
			newSmallCavesVisited.append(nextCave)

		newStartingPath = startingPath.copy()
		newStartingPath.append(nextCave)
			
		newPaths = paths(newStartingPath, newSmallCavesVisited)
		allPaths.extend(newPaths)
	
	return allPaths

print(len(paths(deque(['start']), ['start'])))