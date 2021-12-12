from collections import deque
from statistics import median

f = open('input.txt', 'r')
 
nextClosingBrackets = deque()
autoCompleteScores = []
for line in f.readlines():

	for bracket in line:
		
		if bracket == '(':
			nextClosingBrackets.append(')')
		elif bracket == '[':
			nextClosingBrackets.append(']')
		elif bracket == '{':
			nextClosingBrackets.append('}')
		elif bracket == '<':
			nextClosingBrackets.append('>')
		elif bracket == '\n':
			continue
		elif bracket != nextClosingBrackets.pop():
			nextClosingBrackets = deque()
			break

	autoCompleteScore = 0
	while len(nextClosingBrackets) > 0:
		nextClosingBracket = nextClosingBrackets.pop()

		autoCompleteScore *= 5

		if nextClosingBracket == ')':
			autoCompleteScore += 1
		elif nextClosingBracket == ']':
			autoCompleteScore += 2
		elif nextClosingBracket == '}':
			autoCompleteScore += 3
		elif nextClosingBracket == '>':
			autoCompleteScore += 4

	if autoCompleteScore > 0:
		autoCompleteScores.append(autoCompleteScore)

print(median(autoCompleteScores))