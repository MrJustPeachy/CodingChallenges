data = [int(n) for n in input().strip().split()]

totalRooms = data[0]
bookedRooms = data[1]

availableRooms = totalRooms - bookedRooms

roomsTaken = []

if availableRooms == 0:
    print('too late')
else:

    while bookedRooms > 0:
        roomsTaken.append(int(input().strip()))

        bookedRooms -= 1

    for i in range(1, totalRooms):
        if i not in roomsTaken:
            print(i)
            break