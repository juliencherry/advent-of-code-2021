f = open('input.txt', 'r')

dots = []
foldInstructions = []

for line in f.readlines():
	if line.startswith('\n'):
		continue
	elif line.startswith('fold along x='):
		foldInstructions.append(('x', int(line.rstrip().split('=')[1])))
	elif line.startswith('fold along y='):
		foldInstructions.append(('y', int(line.rstrip().split('=')[1])))
	else:
		x, y = line.rstrip().split(',')
		dots.append((int(x), int(y)))

for foldInstruction in foldInstructions:
	for i, dot in enumerate(dots):
		axis, foldPoint = foldInstruction
		x, y = dot

		if axis == 'x' and (x > foldPoint):
			dots[i] = (2 * foldPoint - x, y)
		elif axis == 'y' and (y > foldPoint):
			dots[i] = (x, 2 * foldPoint - y)

for y in range(0, 6):
	for x in range (0, 40):
		if (x, y) in dots:
			print('#', end='')
		else:
			print('.', end='')
	print('')