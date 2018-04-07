dogs = [int(n) for n in input().strip().split()]
heroes = [int(n) for n in input().strip().split()]

dogA = [dogs[0], dogs[1], dogs[0] + dogs[1]]
dogB = [dogs[2], dogs[3], dogs[2] + dogs[3]]

for hero in heroes:

    attackers = 0



    if hero <= dogA[0]:
        attackers += 1
    elif