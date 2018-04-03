import math

info = input().strip().split()

matches = int(info[0])
boxLength = int(info[1])
boxWidth = int(info[2])

for m in range(matches):
    match = input().strip()

    boxHypotenuse = math.sqrt(math.pow(boxLength, 2) + math.pow(boxWidth, 2))

    if int(match) <= boxWidth or int(match) <= boxLength or int(match) <= boxHypotenuse:
        print("DA")
    else:
        print("NE")