import math

# Import file
filename = 'Prob09.in.txt'


def rotate(strg,n):
    return strg[n:] + strg[:n]


with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        textToEncode = file.readline().strip()
        keyword = file.readline().strip() * 5

        alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()

        newString = ''
        letterPos = 0

        for i in range(len(textToEncode)):

            encodeChar = textToEncode[i]
            keywordChar = keyword[letterPos]

            if encodeChar != ' ':
                startingIndex = alphabet.index(keywordChar)
                encodeString = rotate(alphabet, alphabet.index(encodeChar))
                newString += encodeString[startingIndex]
                letterPos += 1

            else:
                newString += ' '

        print(newString)

        test_cases -= 1