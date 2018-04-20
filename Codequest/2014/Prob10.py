# Import file
filename = 'Prob01.in.txt'

# keyDict = {
#     'q': '\t',
#     'w': 'q',
#     'e': 'w'
# }

topRow = 'qwertyuiop'
newTopRow = '\tqwertyuio'

homeRow = 'asdfghjkl'
newHomeRow = 'asdfghjk'

bottomRow = 'zxcvbnm,.'
newBottomRow = 'zxcvbnm,'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        lines = int(file.readline().strip())

        while lines > 0:

            line = file.readline().strip()

            capsLockOn = False
            newLine = ''

            for char in line:
                if char.lower() == 'a':
                    capsLockOn = True
                else:
                    if char.lower() in topRow:
                        newIndex = newTopRow[topRow.index(char.lower()) - 1]

            lines -= 1

        test_cases -= 1