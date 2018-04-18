test_cases = int(input().strip())

while test_cases > 0:

    data = input().strip().split()

    direction = data[0]
    minuteChange = int(data[1])
    currentHour = int(data[2])
    currentMinute = int(data[3])

    if direction == 'F':
        if minuteChange + currentMinute < 60:
            print('%d %d' % (currentHour, currentMinute + minuteChange))
        elif 60 <= minuteChange + currentMinute < 120:
            newMinutes = minuteChange + currentMinute - 60
            if currentHour == 23:
                newHour = 0
            else:
                newHour = currentHour + 1
            print('%d %d' % (newHour, newMinutes))
        else:
            newMinutes = minuteChange + currentMinute - 120
            if currentHour == 23:
                newHour = 1
            elif currentHour == 22:
                newHour = 0
            else:
                newHour = currentHour + 2
            print('%d %d' % (newHour, newMinutes))
    else:
        if currentMinute - minuteChange >= 0:
            print('%d %d' % (currentHour, currentMinute - minuteChange))
        elif 0 > currentMinute - minuteChange >= -60:
            newMinutes = 60 - minuteChange + currentMinute
            if currentHour == 0:
                newHour = 23
            else:
                newHour = currentHour - 1
            print('%d %d' % (newHour, newMinutes))
        else:
            newMinutes = 120 - minuteChange + currentMinute
            if currentHour == 0:
                newHour = 22
            elif currentHour == 1:
                newHour = 23
            else:
                newHour = currentHour - 2
            print('%d %d' % (newHour, newMinutes))

    test_cases -= 1
