import sys

for file in sys.stdin:

    if file.strip() == '0':
        break

    N = int(file.strip())
    N_summed = sum(map(int, str(N)))

    for i in range(11, 100000):
        multiplied = sum(map(int, str(N * i)))

        if N_summed == multiplied:
            print(i)
            break
