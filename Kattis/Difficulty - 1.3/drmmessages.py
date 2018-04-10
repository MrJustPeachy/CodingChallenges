string = input().strip()

firstHalf = string[:int(len(string) / 2)]
secondHalf = string[int(len(string) / 2):]

firstValue = sum([ord(letter) - 65 for letter in firstHalf])
secondValue = sum([ord(letter) - 65 for letter in secondHalf])

ordFirst = [ord(letter) - 65 for letter in firstHalf]
ordSecond = [ord(letter) - 65 for letter in secondHalf]

rotatedFirst = ''
rotatedSecond = ''

finalMessage = ''

for num in ordFirst:
    rotation = firstValue % 26

    if num + rotation > 26:
        diff = (num + rotation) % 26

        rotatedFirst += chr(diff + 65)
    else:
        rotatedFirst += chr(num + rotation + 65)

for num in ordSecond:
    rotation = secondValue % 26

    if num + rotation > 26:
        diff = (num + rotation) % 26

        rotatedSecond += chr(diff + 65)
    else:
        rotatedSecond += chr(num + rotation + 65)

for i in range(len(rotatedFirst)):
    firstLetter = ord(rotatedFirst[i]) - 65
    secondLetter = ord(rotatedSecond[i]) - 65

    if firstLetter + secondLetter > 26:
        diff = (firstLetter + secondLetter) % 26

        finalMessage += chr(diff + 65)
    else:
        if chr(firstLetter + secondLetter + 65) == '[':
            finalMessage += 'A'
        else:
            finalMessage += chr(firstLetter + secondLetter + 65)


print(finalMessage)
