from collections import deque

f = open('input.txt', 'r')
 
nextClosingBrackets = deque()
syntaxErrorScore = 0
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
		else:
			if bracket == nextClosingBrackets.pop():
				continue
			elif bracket == ')':
				syntaxErrorScore += 3
			elif bracket == ']':
				syntaxErrorScore += 57
			elif bracket == '}':
				syntaxErrorScore += 1197
			elif bracket == '>':
				syntaxErrorScore += 25137
			break

print(syntaxErrorScore)