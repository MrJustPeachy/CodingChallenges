
filename = 'Prob04.in.txt'

for line in open(filename):

    nums = sorted([int(n) for n in line.strip().split(',')])

    print(','.join([str(n) for n in nums]))
