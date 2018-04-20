import operator

# Import file
filename = 'Prob08.in.txt'


def computeFactorial(n):
    number = 1

    for i in range(1, n + 1):
        number *= i

    return number


for line in open(filename):

    enemies, numberOfMissiles = [int(n) for n in line.strip().split()]

    enemiesFactorial = computeFactorial(enemies)
    missilesFactorial = computeFactorial(numberOfMissiles)
    denom = missilesFactorial * (computeFactorial(enemies - numberOfMissiles))

    print(int(enemiesFactorial / denom))
