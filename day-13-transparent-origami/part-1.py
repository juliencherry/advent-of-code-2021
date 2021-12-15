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

for i, dot in enumerate(dots):
	axis, foldPoint = foldInstructions[0]
	x, y = dot

	if axis == 'x' and (x > foldPoint):
		dots[i] = (2 * foldPoint - x, y)
	elif axis == 'y' and (y > foldPoint):
		dots[i] = (x, 2 * foldPoint - y)

print(len(list(set(dots))))