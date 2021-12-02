import sys

f = open('input.txt', 'r')

horizontalPos = 0
depth = 0
aim = 0

for line in f.readlines():
    if line.startswith('forward '):
        x = int(line[len('forward ')])
        horizontalPos += x
        depth += aim * x
        continue
    if line.startswith('up '):
        aim -= int(line[len('up ')])
        continue
    if line.startswith('down '):
        aim += int(line[len('down ')])
        continue

print(horizontalPos * depth)

    
