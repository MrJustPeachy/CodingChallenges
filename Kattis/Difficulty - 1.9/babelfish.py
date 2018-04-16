import sys

dictionary = {}

for line in sys.stdin:

    if line.strip() == '':
        break

    translation, foreignWord = line.strip().split()

    dictionary[foreignWord] = translation

for line in sys.stdin:

    if line == '\n':
        break

    if line.strip() in dictionary:
        print(dictionary[line.strip()])
    else:
        print('eh')
