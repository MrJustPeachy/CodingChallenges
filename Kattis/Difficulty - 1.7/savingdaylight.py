import sys

for line in sys.stdin:

    if line == '\n':
        break

    data = [n for n in line.strip().split()]

    date = '%s %s %s' % (data[0], data[1], data[2])

    sunrise = data[3].split(':')
    sunset = data[4].split(':')

    sunriseHours = int(sunrise[0])
    sunriseMinutes = int(sunrise[1])

    sunsetHours = int(sunset[0])
    sunsetMinutes = int(sunset[1])

    hours = 0
    minutes = 0

    if sunriseMinutes > sunsetMinutes:
        hours = sunsetHours - sunriseHours - 1
        minutes = sunsetMinutes + (60 - sunriseMinutes)
    else:
        hours = sunsetHours - sunriseHours
        minutes = sunsetMinutes - sunriseMinutes

    print('%s %d hours %d minutes' % (date, hours, minutes))