test_cases = int(input().strip())

cups = []

while test_cases > 0:

    data = [n for n in input().strip().split()]

    radius = 0
    color = ''

    try:
        radius = int(data[0]) // 2
        color = data[1]
    except ValueError:
        radius = int(data[1])
        color = data[0]

    cups.append([color, radius])

    test_cases -= 1

sortedCups = sorted(cups, key=lambda l: l[1])

for cup in sortedCups:
    print(cup[0])