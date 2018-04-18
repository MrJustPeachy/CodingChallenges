numberOfSeedlings = int(input().strip())
seedlings = sorted([int(n) for n in input().strip().split()])
seedlings.reverse()
highestDays = 0

for i in range(len(seedlings)):
    daysToGrow = seedlings[i] + i + 1

    if daysToGrow > highestDays:
        highestDays = daysToGrow

print(highestDays + 1)