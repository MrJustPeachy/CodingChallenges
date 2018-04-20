# Import file
filename = 'Prob03.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        nums = [int(n) for n in file.readline().strip().split()]

        added = nums[0] + nums[1]
        multiplied = nums[0] * nums[1]

        print('%d %d' % (added, multiplied))

        test_cases -= 1