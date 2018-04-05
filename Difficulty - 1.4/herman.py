import math

radius = int(input().strip())
area = round((math.pi * math.pow(radius, 2)), 6)
hypotenuse = math.sqrt(math.pow(radius, 2) * 2)
triangleArea = ((0.5 * (radius * radius)) * 4)

print(area)
print('{:.6f}'.format(triangleArea))