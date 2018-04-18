import sys
import re

vowels = ['a', 'e', 'i', 'o', 'u', 'y']

for line in sys.stdin:

    if line == '\n':
        break

    message = line.strip().split()

    for word in message:
        if word[0] in vowels:
            print(word + 'yay ', end='')
        else:
            print(re.sub(r'^([^aeiouy]*)(\w*)', '\\2\\1ay ', word), end='')

    print()
