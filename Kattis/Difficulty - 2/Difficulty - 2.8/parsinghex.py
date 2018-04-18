import sys
import re


for line in sys.stdin:

    testString = line.strip()

    possibleHex = re.findall(r'0x[0-9A-F]+', testString, re.I)

    for hex in possibleHex:
        print('%s %d' % (hex, int(hex, 16)))