import sys

coords = []

for line in sys.stdin:

    points = int(line.strip())
    coords.append(points)

x = int(coords[0])
y = int(coords[1])

# Q1
if x > 0 and y > 0:
    print(1)

# Q2
if x < 0 and y > 0:
    print(2)

# Q3
if x < 0 and y < 0:
    print(3)

# Q4
if x > 0 and y < 0:
    print(4)
