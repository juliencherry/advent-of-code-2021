f = open('input.txt', 'r')

timesDigits1478Appear = 0
for line in f.readlines():
	outputValues = line.split(' | ')[1][:-1].split(' ')
	for val in outputValues:
		if len(val) == 2 or len(val) == 4 or len(val) == 3 or len(val) == 7:
			timesDigits1478Appear += 1
	
print(timesDigits1478Appear)