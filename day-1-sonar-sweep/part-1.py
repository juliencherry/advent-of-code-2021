import sys

f = open('input.txt', 'r')

previousLine = sys.maxsize
numIncreases = 0

for line in f.readlines():
    if int(line) > previousLine:
        numIncreases += 1
    previousLine = int(line)

print(numIncreases)

    
