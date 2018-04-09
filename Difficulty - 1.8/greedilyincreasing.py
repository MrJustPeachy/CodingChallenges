length = int(input().strip())

nums = [int(n) for n in input().strip().split()]

increasingNums = []

for i in range(len(nums)):

    if i == 0:
        increasingNums.append(nums[i])
    else:
        if nums[i] > increasingNums[-1]:
            increasingNums.append(nums[i])

print(len(increasingNums))

for num in increasingNums:
    print('%d ' % num, end='')