inputAmount = int(input().strip())

teams = []

while inputAmount > 0:

    team = input().strip().split()

    teams.append([team[0], team[1]])

    inputAmount -= 1

print(set(tuple(element) for element in teams))