import re

# Import file
filename = 'Prob11.in.txt'

for line in open(filename):

    operation, objectType, name = line.strip().split(';')

    if operation == 'S':
        wordList = re.findall('[a-zA-Z][a-z]*', name)
        print(' '.join(wordList).lower())
    else:
        wordList = re.findall('[a-zA-Z][a-z]*', name)
        for i in range(len(wordList)):
            if i != 0:
                wordList[i] = wordList[i].title()
        # print(wordList)
        if objectType == 'M':
            print(wordList[0].lower(), end='')
            print(''.join(wordList[1:]), end='')
            print('()')
        elif objectType == 'V':
            print(wordList[0].lower(), end='')
            print(''.join(wordList[1:]))
        elif objectType == 'C':
            print(''.join(wordList))
