import sys

f = open('input.txt', 'r')

firstWindow = []
secondWindow = []
numIncreases = 0

for line in f.readlines():
    if len(firstWindow) < 3:
        firstWindow.append(int(line))
        continue

    secondWindow = firstWindow.copy()
    secondWindow.pop(0)
    secondWindow.append(int(line))

    if sum(secondWindow) > sum(firstWindow):
        numIncreases += 1

    firstWindow = secondWindow

print(numIncreases)

    
