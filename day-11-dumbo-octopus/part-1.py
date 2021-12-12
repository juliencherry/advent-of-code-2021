f = open('input.txt', 'r')
 
octopusEnergyLevels = []
rows = 10
columns = 10

for row in f.readlines():
	octopusEnergyLevels.append(list(map(int, list(row)[:-1]))) 

flashes = 0
for step in range(0, 100):
	
	octopodesToFlash = []
	for i, row in enumerate(octopusEnergyLevels):
		for j, _ in enumerate(row):
			octopusEnergyLevels[i][j] += 1
			if octopusEnergyLevels[i][j] == 10:
				octopodesToFlash.append((i, j))
				
	while (len(octopodesToFlash) > 0):
		x, y = octopodesToFlash.pop()
		flashes += 1

		for i in range(-1, 2):
			for j in range(-1, 2):
				if i == 0 and j == 0:
					continue

				elif x + i < 0 or x + i >= rows or y + j < 0 or y + j >= columns:
					continue
				
				octopusEnergyLevels[x + i][y + j] += 1
				if octopusEnergyLevels[x + i][y + j] == 10:
					octopodesToFlash.append((x + i, y + j))
	
	for i, row in enumerate(octopusEnergyLevels):
		for j, _ in enumerate(row):
			if octopusEnergyLevels[i][j] > 9:
				octopusEnergyLevels[i][j] = 0

print(flashes)