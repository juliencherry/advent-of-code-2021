f = open('input.txt', 'r')
lanternfish = list(map(int, f.readlines()[0].split(',')))

expiringFishAtDay = [0] * 256

for fish in lanternfish:
	expiringFishAtDay[fish] += 1

finalCount = 0

for day, numFish in enumerate(expiringFishAtDay):
	if day + 6 + 1 >= len(expiringFishAtDay):
		finalCount += numFish
	else:
		expiringFishAtDay[day + 6 + 1] += numFish	

	if day + 8 + 1 >= len(expiringFishAtDay):
		finalCount += numFish
	else:
		expiringFishAtDay[day + 8 + 1] += numFish	

print(finalCount)