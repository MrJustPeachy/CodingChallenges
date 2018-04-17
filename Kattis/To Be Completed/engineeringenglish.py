import sys
from collections import Counter
import re

string = ''

for line in sys.stdin:

    if line == '\n':
        break

    string += line

stringList = string.lower().split()
wordCount = Counter(stringList).most_common()

print(wordCount)

for word in wordCount:
    if word[1] == 1:
        break

    countsOfWord = word[1]

    replace = r"\b(?=\w)" + word[0] + r"\b(?!\w)"
    print(replace)

    print(re.sub(replace, '.', string.strip(), countsOfWord, re.IGNORECASE))

# print(string)