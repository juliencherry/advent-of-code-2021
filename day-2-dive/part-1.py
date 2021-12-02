import sys

f = open('input.txt', 'r')

horizontalPos = 0
depth = 0

for line in f.readlines():
    if line.startswith('forward '):
        horizontalPos += int(line[len('forward ')])
        continue
    if line.startswith('up '):
        depth -= int(line[len('up ')])
        continue
    if line.startswith('down '):
        depth += int(line[len('down ')])
        continue

print(horizontalPos * depth)

    
