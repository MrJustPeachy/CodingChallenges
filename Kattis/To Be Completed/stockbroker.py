daysInPast = int(input().strip())

pastAmounts = []

while daysInPast > 0:

    pastAmounts.append(int(input().strip()))

    daysInPast -= 1

sharesOwned = 0
dayBalance = 100

for i in range(len(pastAmounts) - 1):
    if i == 0 and pastAmounts[0] <= 100:
        sharesOwned = 100 // pastAmounts[0]
        dayBalance -= (100 // pastAmounts[0]) * pastAmounts[0]
    elif pastAmounts[i] > pastAmounts[i + 1]:
        dayBalance += pastAmounts[i] * sharesOwned
        sharesOwned = 0
    elif pastAmounts[i] < pastAmounts[i + 1]:
        if dayBalance >= pastAmounts[i]:
            sharesOwned += dayBalance // pastAmounts[i]
            dayBalance -= (dayBalance // pastAmounts[i]) * pastAmounts[i]

total = (sharesOwned * pastAmounts[-1]) + dayBalance
print(total)