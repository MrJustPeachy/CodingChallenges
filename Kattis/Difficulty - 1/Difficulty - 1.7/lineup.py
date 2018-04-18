test_cases = int(input().strip())

names = []

while test_cases > 0:

    names.append(input().strip())

    test_cases -= 1

namesIncreasing = sorted(names)
namesDecreasing = sorted(names, reverse=True)

if names == namesIncreasing:
    print('INCREASING')
elif names == namesDecreasing:
    print('DECREASING')
else:
    print('NEITHER')