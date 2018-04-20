# Import file
filename = 'Prob04.in.txt'

decodingKey = ''
cipherList = []

for line in open(filename):

    if len(decodingKey) == 0:
        decodingKey += line.strip()
    else:
        cipherList.append(line.strip().split())

for cipher in cipherList:
    newString = ''
    for individualCipher in cipher:
        for char in individualCipher.split('-'):
            newString += decodingKey[int(char) - 1]
        newString += ' '

    print(newString)