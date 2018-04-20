import re

# Import file
filename = 'Prob11.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        line = file.readline().strip().split()

        newLine = []

        for word in line:
            reversedWord = re.sub(r'\b\S*\b', lambda m: m.group(0)[::-1], word)

            newString = ''

            for i in range(len(reversedWord)):
                if word[i].isupper():
                    newString += reversedWord[i].upper()
                else:
                    newString += reversedWord[i].lower()

            newLine.append(newString)

        print(' '.join(newLine))

        test_cases -= 1