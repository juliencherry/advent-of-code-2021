import sys

f = open('input.txt', 'r')

polymerTemplate = ''
pairInsertionRules = dict()
elements = []

for i, line in enumerate(f.readlines()):
	if i == 0:
		polymerTemplate = line.rstrip()
		continue

	if i == 1:
		continue

	pair, elementToInsert = line.rstrip().split(' -> ')
	pairInsertionRules[pair] = elementToInsert

	if not elementToInsert in elements:
		elements.append(elementToInsert)

for i in range(0, 10):
	newPolymerTemplate = ''

	for j, element in enumerate(polymerTemplate):
		if j >= len(polymerTemplate) - 1:
			newPolymerTemplate += element
			continue

		pair = element + polymerTemplate[j + 1]
		newPolymerTemplate += pair[0] + pairInsertionRules[pair]
	
	polymerTemplate = newPolymerTemplate

leastCommonElementQuantity = sys.maxsize
mostCommonElementQuantity = 0

for element in elements:
	elementQuantity = polymerTemplate.count(element)

	if elementQuantity < leastCommonElementQuantity:
		leastCommonElementQuantity = elementQuantity
	
	if elementQuantity > mostCommonElementQuantity:
		mostCommonElementQuantity = elementQuantity

print(mostCommonElementQuantity - leastCommonElementQuantity)