import math

data = input().strip().split()

height = int(data[0])
angle = int(data[1])

# sin(angle) = height / length
# length * sin(angle) = height
# length = height/ sin(angle)

length = height / math.sin(math.radians(angle))

print(math.ceil(length))