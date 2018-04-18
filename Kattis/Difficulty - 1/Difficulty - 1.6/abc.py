nums = sorted([int(n) for n in input().strip().split()])
chars = input().strip()

order = []

for char in chars:

    for i in range(len(nums)):
        if i == 0 and char == 'A':
            print('%d ' % nums[i], end='')
        elif i == 1 and char == 'B':
            print('%d ' % nums[i], end='')
        elif i == 2 and char == 'C':
            print('%d ' % nums[i], end='')