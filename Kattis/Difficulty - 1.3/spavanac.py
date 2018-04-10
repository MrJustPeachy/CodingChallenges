data = input().strip().split()

hours = int(data[0])
minutes = int(data[1])

hourTime = 0
minuteTime = 0

if minutes >= 45:
    hourTime = hours
    minuteTime = minutes - 45
else:

    if hours > 0:
        hourTime = hours - 1
    else:
        hourTime = 23

    minuteDiff = minutes - 45

    minuteFixed = 60 + minuteDiff

    minuteTime = minuteFixed

print(str(hourTime) + ' ' + str(minuteTime))