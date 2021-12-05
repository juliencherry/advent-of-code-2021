hydrothermalVents = [[0]*1000 for i in range(1000)]
numOverlaps = 0

f = open('input.txt', 'r')
for i, line in enumerate(f.readlines()):
	line = line.replace(' -> ', ",")
	startX, startY, endX, endY = list(map(int, line.split(',')))

	xIncrement = 1
	yIncrement = 1

	if startX > endX:
		xIncrement = -1
	if startY > endY:
		yIncrement = -1

	if startX == endX:
		for y in range(startY, endY + yIncrement, yIncrement):
			hydrothermalVents[startX][y] += 1

			if hydrothermalVents[startX][y] == 2:
				numOverlaps += 1
	elif startY == endY:
		for x in range(startX, endX + xIncrement, xIncrement):
			hydrothermalVents[x][startY] += 1

			if hydrothermalVents[x][startY] == 2:
				numOverlaps += 1
	else:
		for x, y in zip(range(startX, endX + xIncrement, xIncrement), range(startY, endY + yIncrement, yIncrement)):
			hydrothermalVents[x][y] += 1

			if hydrothermalVents[x][y] == 2:
				numOverlaps += 1

print(numOverlaps)