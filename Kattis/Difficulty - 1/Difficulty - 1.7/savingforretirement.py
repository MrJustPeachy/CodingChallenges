import math

data = [int(n) for n in input().strip().split()]

bobAge = data[0]
bobRetireYear = data[1]
bobSavingYear = bobRetireYear - bobAge
bobSavings = data[2] * bobSavingYear
aliceAge = data[3]
aliceSaving = data[4]
yearsDifference = math.ceil(bobSavings / aliceSaving)
aliceRetireAge = aliceAge + yearsDifference

if yearsDifference * aliceSaving == bobSavings:
    aliceRetireAge += 1
    print(aliceRetireAge)
else:
    print(aliceRetireAge)