import math

info = input().split()

articles = int(info[0])
impact = int(info[1])

lowest_impact = impact - 0.99

scientists = math.ceil(lowest_impact * articles)

print(scientists)