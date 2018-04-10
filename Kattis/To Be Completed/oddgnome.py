test_cases = int(input().strip())

while test_cases > 0:

    gnomes = [int(n) for n in input().strip().split()][1:-1]

    kingPos = 0

    sortedGnomes = sorted(gnomes)

    print(gnomes)

    for i in range(len(gnomes)):
        print(i)
        if i == 0:
            if gnomes[i] > gnomes[i + 1]:
                kingPos = i
                break
        elif i < len(gnomes) - 1:
            if (gnomes[i] > gnomes[i + 1] and gnomes[i - 1]) or (gnomes[i] < gnomes[i - 1]):
                kingPos = i
        else:
            if gnomes[i] < gnomes[i - 1]:
                kingPos = i
                break

    print(kingPos)

    test_cases -= 1
