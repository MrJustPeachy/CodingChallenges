import sys

for line in sys.stdin:

    if line == '\n':
        break

    if line.strip() == '0':
        break

    originalString = [n for n in line.strip().split()]

    rotation = int(originalString[0])
    message = originalString[1][::-1]

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.'

    encryptedMessage = ''

    for char in message:
        position = alphabet.index(char)

        if position + rotation < len(alphabet):
            encryptedMessage += alphabet[position + rotation]
        elif position + rotation > len(alphabet):
            difference = position + rotation - len(alphabet)
            encryptedMessage += alphabet[difference]
        elif position + rotation == len(alphabet):
            encryptedMessage += alphabet[0]

    print(encryptedMessage)