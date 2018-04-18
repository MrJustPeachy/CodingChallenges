initialBoxHolder = int(input().strip())
questions = int(input().strip())

timeRemaining = 210
boxHolder = 0

while questions > 0:

    playerInfo = input().strip().split()
    timeUsed = int(playerInfo[0])
    answer = playerInfo[1]

    timeRemaining -= timeUsed

    if timeRemaining <= 0:
        if boxHolder == 0:
            print(initialBoxHolder)
        else:
            print(boxHolder)
        break

    if answer == 'T':
        if boxHolder == 0:
            if initialBoxHolder == 8:
                boxHolder = 1
            else:
                boxHolder = initialBoxHolder + 1
        elif boxHolder == 8:
            boxHolder = 1
        else:
            boxHolder += 1

    questions -= 1
