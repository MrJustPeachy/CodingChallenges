import math

# Import file
filename = 'Prob04.in.txt'


def findIndex(n):
    fibo = 2.078087 * math.log(n) + 1.672276

    # returning rounded off value of index
    return round(fibo)


with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        index = int(file.readline().strip())
        fibNum = findIndex(index)

        print('%d = %d' % (index, fibNum))

        test_cases -= 1