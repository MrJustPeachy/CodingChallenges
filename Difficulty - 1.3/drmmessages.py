string = input().strip()

firstHalf = string[:int(len(string) / 2)]
secondHalf = string[int(len(string) / 2):]

for l in firstHalf:
    print(ord(l))
    print(l)

firstValue = sum([ord(letter) for letter in firstHalf])
secondValue = sum([ord(letter) for letter in secondHalf])

print(firstValue)
print(secondValue)