import math
import collections

# Import file
filename = 'Prob09.in.txt'

setNum = 1

for line in open(filename):

    nums = sorted([int(n) for n in line.strip().split(',')])

    mean = sum(nums) / len(nums)
    if len(nums) % 2 == 0:
        leftMedian = nums[int(len(nums) / 2) - 1]
        rightMedian = nums[int(len(nums) / 2)]
        median = (leftMedian + rightMedian) / 2
    else:
        median = nums[int(len(nums) / 2)]

    mostCommon = collections.Counter(nums).most_common()
    highestNum = mostCommon[0][1]
    mostCommonFiltered = [n for n in mostCommon if n[1] >= highestNum]

    mode = []

    for num in mostCommonFiltered:
        mode.append(str(num[0]))

    if len(nums) % 2 == 0:
        print('Set {:d}: Mean={:.1f}, Median={:.1f}, Mode='.format(setNum, mean, median), end='')
    else:
        print('Set {:d}: Mean={:.1f}, Median={:d}, Mode='.format(setNum, mean, median), end='')
    print(','.join(mode))

    setNum += 1
