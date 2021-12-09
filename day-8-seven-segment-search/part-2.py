f = open('input.txt', 'r')

totalOutputValue = 0
for line in f.readlines():
	signalPatterns, outputValues = line[:-1].split(' | ')
	signalPatterns = signalPatterns.split(' ')
	outputValues = list(map(set, outputValues.split(' ')))
	
	signalLinesToDigit = [set()] * 10

	# First pass: find 1, 4, 7, and 8 
	remainingSignalPatterns = []
	for signalPattern in signalPatterns:

		# digit is 1
		if len(signalPattern) == 2:
			signalLinesToDigit[1] = set(list(signalPattern))
			continue

		# digit is 4
		if len(signalPattern) == 4:
			signalLinesToDigit[4] = set(list(signalPattern))
			continue

		# digit is 7
		if len(signalPattern) == 3:
			signalLinesToDigit[7] = set(list(signalPattern))
			continue

		# digit is 8
		if len(signalPattern) == 7:
			signalLinesToDigit[8] = set(list(signalPattern))
			continue

		remainingSignalPatterns.append(signalPattern)
	signalPatterns = remainingSignalPatterns

	# Second pass: find 3
	remainingSignalPatterns = []
	for signalPattern in signalPatterns:
		if len(signalPattern) == 5:
			signalLines = set(list(signalPattern))

			# digit is 3
			if len(signalLines - signalLinesToDigit[7]) == 2:
				signalLinesToDigit[3] = signalLines
				continue

		remainingSignalPatterns.append(signalPattern)
	signalPatterns = remainingSignalPatterns

	# Third pass: find 2, 5, and 9
	remainingSignalPatterns = []
	for signalPattern in signalPatterns:
		signalLines = set(list(signalPattern))

		if len(signalPattern) == 5:

			# digit is 2
			if len(signalLines - signalLinesToDigit[4]) == 3:
				signalLinesToDigit[2] = signalLines
				continue
			
			# digit is 5
			else:
				signalLinesToDigit[5] = signalLines
				continue
		
		if len(signalPattern) == 6:

			# digit is 9
			if len(signalLines - signalLinesToDigit[3]) == 1:
				signalLinesToDigit[9] = signalLines
				continue

		remainingSignalPatterns.append(signalPattern)
	signalPatterns = remainingSignalPatterns

	# Fourth pass: find 0 and 6
	remainingSignalPatterns = []
	for signalPattern in signalPatterns:
		if len(signalPattern) == 6:
			signalLines = set(list(signalPattern))

			# digit is 0
			if len(signalLines - signalLinesToDigit[5]) == 2:
				signalLinesToDigit[0] = signalLines
				continue
			
			# digit is 6
			else:
				signalLinesToDigit[6] = signalLines
				continue

		remainingSignalPatterns.append(signalPattern)
	signalPatterns = remainingSignalPatterns


	value = ''
	for outputValue in outputValues: 
		for digit, signalLine in enumerate(signalLinesToDigit):
			if outputValue == signalLine:
				value += str(digit)
				continue

	totalOutputValue += int(value)

print(totalOutputValue)