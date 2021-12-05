hydrothermalVents = [[0]*1000 for i in range(1000)]
numOverlaps = 0

f = open('input.txt', 'r')
for i, line in enumerate(f.readlines()):
	line = line.replace(' -> ', ",")
	startX, startY, endX, endY = list(map(int, line.split(',')))
	increment = 1

	if startX == endX:

		if startY > endY:
			increment = -1

		for y in range(startY, endY + increment, increment):
			hydrothermalVents[startX][y] += 1

			if hydrothermalVents[startX][y] == 2:
				numOverlaps += 1

		continue

	if startY == endY:

		if startX > endX:
			increment = -1

		for x in range(startX, endX + increment, increment):
			hydrothermalVents[x][startY] += 1

			if hydrothermalVents[x][startY] == 2:
				numOverlaps += 1

print(numOverlaps)