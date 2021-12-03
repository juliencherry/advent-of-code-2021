import sys

def mostCommonBits(bitList):
    bitCount = [0] * 12
    for bits in bitList:
        for i, bit in enumerate(bits):
            if bit == '\n':
                continue
            elif int(bit) == 0:
                bitCount[i] -= 1
            else:
                bitCount[i] += 1

    return [int(bits >= 0) for bits in bitCount]

f = open('input.txt', 'r')

bitList = f.readlines()

oxygenBitList = list(bitList)
co2BitList = list(bitList)
oxygenGeneratorRating = 0
co2ScrubberRating = 0

for i in range(0, 12):

    newOxygenBitList = [bits for bits in oxygenBitList if int(bits[i]) == mostCommonBits(oxygenBitList)[i]]
    newCO2BitList = [bits for bits in co2BitList if int(bits[i]) != mostCommonBits(co2BitList)[i]]

    if len(newOxygenBitList) == 0:
        continue

    oxygenBitList = newOxygenBitList

    if len(newCO2BitList) == 0:
        continue

    co2BitList = newCO2BitList

oxygenGeneratorRating = int(oxygenBitList[0], 2)
co2ScrubberRating = int(co2BitList[0], 2)

print(oxygenGeneratorRating * co2ScrubberRating)

