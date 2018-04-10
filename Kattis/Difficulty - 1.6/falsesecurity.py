import sys

morseCodeDict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '_': '..--',
    ',': '.-.-',
    '.': '---.',
    '?': '----',
}

for line in sys.stdin:

    message = line.strip()

    morseCodeMessage = ''
    breaks = ''

    for char in message:

        code = morseCodeDict

        morseCodeMessage += morseCodeDict[char]
        breaks += str(len(morseCodeDict[char]))

    counter = 0

    decryptedMessage = ''

    for length in breaks[::-1]:
        morseCodeLetter = morseCodeMessage[counter:(counter + int(length))]

        for letter, mcLetter in morseCodeDict.items():
            if mcLetter == morseCodeLetter:
                decryptedMessage += letter

        counter += int(length)

    print(decryptedMessage)