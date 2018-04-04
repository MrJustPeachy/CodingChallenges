import sys

for file in sys.stdin:

    if file.strip() == '0':
        break

    N = sum(map(int, file.strip()))

    for i in range(10, 100000):
        multiplied = sum(map(int, str(N * i)))

        if N == multiplied:
            print(i)
            break