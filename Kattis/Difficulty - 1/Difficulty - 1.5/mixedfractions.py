import sys

for line in sys.stdin:

    if line == '\n':
        break

    if line.strip() == '0 0':
        break

    data = [int(n) for n in line.strip().split()]

    numerator = data[0]
    denominator = data[1]

    wholeNum = numerator // denominator
    remainder = numerator % denominator

    print('%d %d / %d' % (wholeNum, remainder, denominator))