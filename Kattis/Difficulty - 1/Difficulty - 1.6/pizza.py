import math

data = [int(n) for n in input().strip().split()]

radius = data[0]
crust = data[1]
cheese = radius - crust

if radius == crust:
    print('0.000000')
else:
    innerPizza = math.pi * math.pow(radius, 2)
    outerPizza = math.pi * math.pow(cheese, 2)

    print('{:.6f}'.format((outerPizza / innerPizza) * 100))