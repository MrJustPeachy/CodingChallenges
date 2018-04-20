# Import file
filename = 'Prob03.in.txt'

for line in open(filename):

    try:
        nums = [int(n) for n in line.strip().split()]

        numsAscending = sorted(nums)
        numsDescending = sorted(nums, reverse=True)

        if nums == numsAscending:
            print('The numbers are in ascending order')
        elif nums == numsDescending:
            print('The numbers are in descending order')
        else:
            print('The numbers are in random order')

    except ValueError:
        print('The input was invalid')