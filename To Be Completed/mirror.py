test_cases = int(input().strip())

tests = 1

while test_cases > 0:

    grid = [int(n) for n in input().strip().split()]
    rows = grid[0]
    columns = grid[1]

    matrix = []

    while rows > 0:

        matrix.append(input().strip())

        rows -= 1

    print('Test %d' % tests)

    for i in reversed(range(len(matrix))):
        if i == 0:
            print(matrix[i][::-1], end='')
        else:
            print(matrix[i][::-1])

    tests += 1
    test_cases -= 1