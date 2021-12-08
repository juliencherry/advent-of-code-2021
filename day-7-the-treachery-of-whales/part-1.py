from statistics import median 

f = open('input.txt', 'r')
crabs = list(map(int, f.readlines()[0].split(',')))
median = median(crabs)

fuel = 0
for crab in crabs:
	fuel += int(abs(median - crab))

print(fuel)