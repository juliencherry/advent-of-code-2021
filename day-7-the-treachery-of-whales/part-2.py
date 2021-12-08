import sys

f = open('input.txt', 'r')
crabs = list(map(int, f.readlines()[0].split(',')))

bestFuel = sys.maxsize
for alignmentPos in range(min(crabs), max(crabs)):
	fuel = 0
	for crab in crabs:
		distance = int(abs(alignmentPos - crab)) 
		fuel += int(distance * (distance + 1) / 2)
	
	if fuel < bestFuel:
		bestFuel = fuel

print(bestFuel)
