# Import file
filename = 'Prob07.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        regularMessageLines = int(file.readline().strip())

        regMessage = ''

        while regularMessageLines > 0:
            regMessage += file.readline()

            regularMessageLines -= 1

        xCoords, yCoords = [int(n) for n in file.readline().strip().split(',')]

        decoderLines = int(file.readline().strip())

        decoder = ''

        while decoderLines > 0:

            decoder += file.readline()

            decoderLines -= 1

        secretMessage = ''

        for i in range(len(decoder.splitlines())):
            for j in range(len(decoder.splitlines()[i])):
                char = decoder.splitlines()[i][j]
                if char == 'O':
                    secretMessage += regMessage.splitlines()[i + xCoords][j + yCoords]

        print(secretMessage)

        test_cases -= 1