import sys

for line in sys.stdin:

    string = line.strip().lower()

    if string.__contains__('problem'):
        print('yes')
    else:
        print('no')
