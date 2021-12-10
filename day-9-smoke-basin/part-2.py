from collections import deque
from functools import reduce
from operator import mul

f = open('input.txt', 'r')

rows = 100
columns = 100
heightMap = [[]] * rows 
	
for i, line in enumerate(f.readlines()):
	heightMap[i] = list(map(int, list(line)[:-1]))

def pointIsWithinBasin(heightOfAdjacentPoint, row, column):
	if (row < 0 or row >= rows or column < 0 or column >= columns):
		return False
	
	if visited[row][column]:
		return False
	
	point = heightMap[row][column]
	if point >= 9 or point < heightOfAdjacentPoint:
		return False
	
	visited[row][column] = True
	
	return True

basinSizes = []
for i, row in enumerate(heightMap):
	for j, point in enumerate(row):

		isLowPoint = True
		if i > 0 and point >= heightMap[i - 1][j]:
			isLowPoint = False
		if i < rows - 1 and point >= heightMap[i + 1][j]:
			isLowPoint = False
		if j > 0 and point >= heightMap[i][j - 1]:
			isLowPoint = False
		if j < columns - 1 and point >= heightMap[i][j + 1]:
			isLowPoint = False

		if not isLowPoint:
			continue

		basinQueue = deque()
		basinQueue.append((-1, i, j))
		visited = [[False] * columns for _ in range(rows)]
		basinSize = 0

		while basinQueue:
			heightOfAdjacentPoint, row, column = basinQueue.pop()
			if pointIsWithinBasin(heightOfAdjacentPoint, row, column):
				basinSize += 1
				basinQueue.append((heightMap[row][column], row - 1, column))
				basinQueue.append((heightMap[row][column], row + 1, column))
				basinQueue.append((heightMap[row][column], row, column - 1))
				basinQueue.append((heightMap[row][column], row, column + 1))
		
		basinSizes.append(basinSize)

print(reduce(mul, sorted(basinSizes, reverse=True)[:3], 1))