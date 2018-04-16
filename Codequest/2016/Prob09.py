import math

# Import file
filename = 'Prob09.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        data = file.readline().strip().split()

        zoomLevel = int(data[0])
        latitude = float(data[1])
        longitude = float(data[2])

        x = math.floor(abs(((longitude + 180) / 360) * math.pow(2, zoomLevel)))
        y = math.floor(abs(((1 - ((math.log((math.tan(latitude * (math.pi / 180)) + (1 / (math.cos(latitude * (math.pi / 180))))), math.e)) / math.pi))) * math.pow(2, (zoomLevel - 1))))

        print('http://tile.openstreetmap.org/%d/%d/%d.png' % (zoomLevel, x, y))

        test_cases -= 1