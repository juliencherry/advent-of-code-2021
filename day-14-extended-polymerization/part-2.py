from collections import defaultdict
import sys

f = open('input.txt', 'r')

pairCounts = defaultdict(lambda: 0)
pairInsertionRules = dict()

for i, line in enumerate(f.readlines()):
	if i == 0:
		polymerTemplate = line.rstrip()

		for j, element in enumerate(polymerTemplate):
				if j >= len(polymerTemplate) - 1:
					lastElement = element
					continue

				pair = element + polymerTemplate[j + 1]
				pairCounts[pair] += 1
		
		continue

	if line == '\n':
		continue

	pair, elementToInsert = line.rstrip().split(' -> ')
	pairInsertionRules[pair] = elementToInsert

for i in range(0, 40):

	newPairCounts = pairCounts.copy()

	for pair in pairCounts.keys():
		newPairCounts[pair] = 0

	for pair in pairCounts.keys():
		elementToInsert = pairInsertionRules[pair]
		newPairCounts[pair[0] + elementToInsert] += pairCounts[pair]
		newPairCounts[elementToInsert + pair[1]] += pairCounts[pair]
	
	pairCounts = newPairCounts

elementQuantities = defaultdict(lambda: 0)
for pair in pairCounts.keys():
	elementQuantities[pair[0]] += pairCounts[pair]

elementQuantities[lastElement] += 1

leastCommonElementQuantity = sys.maxsize
mostCommonElementQuantity = 0

for elementQuantity in elementQuantities.items():
	element, quantity = elementQuantity
	if quantity < leastCommonElementQuantity:
		leastCommonElementQuantity = quantity
	
	if quantity > mostCommonElementQuantity:
		mostCommonElementQuantity = quantity

print(mostCommonElementQuantity - leastCommonElementQuantity)