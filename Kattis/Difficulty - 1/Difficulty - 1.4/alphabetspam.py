string = input().strip()

stringLength = len(string)
whitespaceChars = 0
lowercaseChars = 0
uppercaseChars = 0
symbols = 0

for char in string:
    if 33 <= ord(char) < 65 or 123 <= ord(char) < 127:
        symbols += 1
    elif 65 <= ord(char) < 91:
        uppercaseChars += 1
    elif 91 <= ord(char) < 97:
        if char == '_':
            whitespaceChars += 1
        else:
            symbols += 1
    elif 97 <= ord(char) < 123:
        lowercaseChars += 1

if whitespaceChars > 0:
    print('{:.8f}'.format(whitespaceChars / stringLength))
else:
    print('0.000000')
if lowercaseChars > 0:
    print('{:.8f}'.format(lowercaseChars / stringLength))
else:
    print('0.000000')
if uppercaseChars > 0:
    print('{:.8f}'.format(uppercaseChars / stringLength))
else:
    print('0.000000')
if symbols > 0:
    print('{:.8f}'.format(symbols / stringLength))
else:
    print('0.000000')
