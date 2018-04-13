test_cases = int(input().strip())

while test_cases > 0:

    data = input().strip().split()

    direction = data[0]
    minuteChange = int(data[1])
    currentHour = int(data[2])
    currentMinute = int(data[3])

    if direction == 'F':
        if minuteChange + currentMinute < 60:
            print('%d %d' % (currentHour, currentMinute))
        else:
            newMinutes = minuteChange + currentMinute - 60
            newHour = currentHour + 1
            if currentHour + 1 > 24:
                newHour = 0
            print('%d %d' % (newHour, newMinutes))
    else:
        if currentMinute - minuteChange >= 0:
            print('%d %d' % (currentHour, currentMinute - minuteChange))
        else:
            newMinutes = 60 - minuteChange + currentMinute
            newHour = currentHour - 1
            if newHour == -1:
                newHour = 23
            print('%d %d' % (newHour, newMinutes))

    test_cases -= 1