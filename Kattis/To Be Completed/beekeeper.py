import sys
from collections import Counter
import re

for line in sys.stdin:

    if line.strip() == '0':
        break

    words = int(line.strip())

    wordList = []

    while words > 0:

        wordList.append(input().strip())

        words -= 1

    vowelCount = []

    for word in wordList:
        print(word)
        vowels = re.findall(r'([aeiouy]{2,})', word)
        print(vowels)