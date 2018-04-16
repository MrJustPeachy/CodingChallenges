# Import file
filename = 'Prob09.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        textLines = int(file.readline().strip())

        text = ''

        while textLines > 0:

            text += file.readline()

            textLines -= 1

        # print(text)
        reflectionType = file.readline().strip()

        if reflectionType == 'X':
            for i in reversed(text.splitlines()):
                print(i)
        elif reflectionType == 'Y':
            for line in text.splitlines():
                print(line[::-1])
        elif reflectionType == 'INVERSE':
            textList = list(map(list, zip(*text.splitlines())))
            for i in textList:
                for j in i:
                    print(j, end='')
                print()

        test_cases -= 1