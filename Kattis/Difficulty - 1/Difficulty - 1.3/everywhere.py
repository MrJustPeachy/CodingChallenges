test_cases = int(input().strip())

while int(test_cases):

    c = int(input().strip())

    cities = []

    while c:

        city = input().strip()
        cities.append(city)

        c -= 1

    print(len(set(cities)))

    test_cases -= 1