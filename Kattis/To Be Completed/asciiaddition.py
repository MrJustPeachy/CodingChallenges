zero = 'xxxxx\n' \
       'x...x\n' \
       'x...x\n' \
       'x...x\n' \
       'x...x\n' \
       'x...x\n' \
       'xxxxx'

one = '....x\n' \
      '....x\n' \
      '....x\n' \
      '....x\n' \
      '....x\n' \
      '....x\n' \
      '....x'

two = 'xxxxx\n' \
      '....x\n' \
      '....x\n' \
      'xxxxx\n' \
      'x....\n' \
      'x....\n' \
      'xxxxx'

three = 'xxxxx\n' \
        '....x\n' \
        '....x\n' \
        'xxxxx\n' \
        '....x\n' \
        '....x\n' \
        'xxxxx'

four = 'x...x\n' \
       'x...x\n' \
       'x...x\n' \
       'xxxxx\n' \
       '....x\n' \
       '....x\n' \
       '....x'

five = 'xxxxx\n' \
       'x....\n' \
       'x....\n' \
       'xxxxx\n' \
       '....x\n' \
       '....x\n' \
       'xxxxx'

six = 'xxxxx\n' \
       'x....\n' \
       'x....\n' \
       'xxxxx\n' \
       'x...x\n' \
       'x...x\n' \
       'xxxxx'

seven = 'xxxxx\n' \
       '....x\n' \
       '....x\n' \
       '....x\n' \
       '....x\n' \
       '....x\n' \
       '....x'

eight = 'xxxxx\n' \
       'x...x\n' \
       'x...x\n' \
       'xxxxx\n' \
       'x...x\n' \
       'x...x\n' \
       'xxxxx'

nine = 'xxxxx\n' \
       'x...x\n' \
       'x...x\n' \
       'xxxxx\n' \
       '....x\n' \
       '....x\n' \
       'xxxxx'


plus = '.....\n' \
       '..x..\n' \
       '..x..\n' \
       'xxxxx\n' \
       '..x..\n' \
       '..x..\n' \
       '.....'

asciiInput = ''
asciiLines = 7

while asciiLines > 0:

    asciiInput += input()

    asciiLines -= 1

asciiNums = []

for i in range(len(asciiInput.splitlines())):
