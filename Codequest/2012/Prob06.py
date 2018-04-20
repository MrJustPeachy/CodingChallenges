import re

# Import file
filename = 'Prob06.in.txt'

for line in open(filename):

    word = re.sub('\s+', '', line.strip().lower())

    wordReversed = re.sub('\s+', '', word[::-1])

    if word == wordReversed:
        print('yes')
    else:
        print('no')