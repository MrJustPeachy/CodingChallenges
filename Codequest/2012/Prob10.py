# Import file
filename = 'Prob10.in.txt'

for line in open(filename):
    number = int(line.strip())

    n = 1

    for i in range(1, number + 1):
        n *= i

    print(n)