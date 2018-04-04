string = input().strip()

firstHalf = string[:int(len(string) / 2)]
secondHalf = string[int(len(string) / 2):]

firstValue = sum([ord(letter) - 65 for letter in firstHalf])
secondValue = sum([ord(letter) - 65 for letter in secondHalf])

ordFirst = [ord(letter) - 65 for letter in firstHalf]
ordSecond = [ord(letter) - 65 for letter in secondHalf]

rotatedFirst = []
rotatedSecond = []

for num in ordFirst:
    