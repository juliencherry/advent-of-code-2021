import sys

f = open('input.txt', 'r')

mostCommonBits = [0] * 12

for bits in f.readlines():
    for i, bit in enumerate(bits):
        if bit == '\n':
            continue
        elif int(bit) == 0:
            mostCommonBits[i] -= 1
        else:
            mostCommonBits[i] += 1

gammaRateStr = ''
for mostCommonBit in mostCommonBits:
    if mostCommonBit > 0:
        gammaRateStr += '1'
    else:
        gammaRateStr += '0'

gammaRate = int(gammaRateStr, 2)
epsilonRate = gammaRate ^ int('111111111111', 2)
print(gammaRate * epsilonRate)
