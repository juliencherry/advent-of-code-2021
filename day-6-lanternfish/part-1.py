f = open('input.txt', 'r')
lanternfish = list(map(int, f.readlines()[0].split(',')))
newLanternfish = list(lanternfish)

for day in range (0, 80):
	for i, fish in enumerate(lanternfish):
		if lanternfish[i] == 0:
			newLanternfish[i] = 6
			newLanternfish.append(8)
		else: 
			newLanternfish[i] -= 1

	lanternfish = list(newLanternfish)

print(len(lanternfish))