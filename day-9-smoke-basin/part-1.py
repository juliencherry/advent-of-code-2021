f = open('input.txt', 'r')

heightMap = [[]] * 100

for i, line in enumerate(f.readlines()):
	heightMap[i] = list(map(int, list(line)[:-1]))

totalRiskLevel = 0
for i, row in enumerate(heightMap):
	for j, cell in enumerate(row):
		isLowPoint = True
		if i > 0 and cell >= heightMap[i - 1][j]:
			isLowPoint = False
		if i < 99 and cell >= heightMap[i + 1][j]:
			isLowPoint = False
		if j > 0 and cell >= heightMap[i][j - 1]:
			isLowPoint = False
		if j < 99 and cell >= heightMap[i][j + 1]:
			isLowPoint = False

		if isLowPoint:
			totalRiskLevel += cell + 1

print(totalRiskLevel)