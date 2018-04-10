'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

smallestMultiple = 0

print(20000 % 20)

for i in range(2520, 10000000):

    multiple = True

    for j in range(1, 21):
        if i % j != 0:
            multiple = False

    if multiple:
        smallestMultiple = i
        break

print(smallestMultiple)