# Import file
filename = 'Prob11.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        action = file.readline().strip()

        cipherKey = file.readline().strip()
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        cipherTestCases = int(file.readline().strip())

        while cipherTestCases > 0:

            message = file.readline().strip()

            newMessage = ''

            for char in message:
                if action == 'ENCRYPT':
                    if char != ' ':
                        charPos = alphabet.index(char.lower())
                        cipherChar = cipherKey[charPos]

                        if char.isupper():
                            newMessage += cipherChar.upper()
                        else:
                            newMessage += cipherChar
                    else:
                        newMessage += ' '
                else:
                    if char != ' ':
                        charPos = cipherKey.index(char.lower())
                        cipherChar = alphabet[charPos]

                        if char.isupper():
                            newMessage += cipherChar.upper()
                        else:
                            newMessage += cipherChar
                    else:
                        newMessage += ' '

            print(newMessage)

            cipherTestCases -= 1

        print()

        test_cases -= 1