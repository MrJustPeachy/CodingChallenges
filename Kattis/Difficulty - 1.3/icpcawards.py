inputAmount = int(input().strip())

teams = []
existing_teams = []

while inputAmount > 0:

    team = input().strip().split()

    if len(teams) < 12:

        if len(existing_teams) > 0:
            try:
                if existing_teams.index(team[0]):
                    pass
            except ValueError:
                teams.append([team[0], team[1]])
                existing_teams.append(team[0])

        else:
            teams.append([team[0], team[1]])
            existing_teams.append(team[0])

    inputAmount -= 1

for i in range(len(teams)):
    print(teams[i][0] + ' ' + teams[i][1])
