data = [int(n) for n in input().strip().split()]

e = data[0]
f = data[1]
c = data[2]

emptyBottles = e + f

bottlesFromEmptyBottles = emptyBottles

print(bottlesFromEmptyBottles)
print(bottlesFromEmptyBottles // c)
print((bottlesFromEmptyBottles // c) // c)
