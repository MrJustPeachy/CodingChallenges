import sys

for line in sys.stdin:

    number = int(line.strip())

    for n in range(number):
        print(str(n + 1) + " Abracadabra")
