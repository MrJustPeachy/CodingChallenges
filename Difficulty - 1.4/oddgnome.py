test_cases = int(input().strip())

while test_cases > 0:

    gnomes = [int(n) for n in input().strip().split()][1:-1]

    kingPos = 0

    sortedGnomes = sorted(gnomes)

    for i in range(0, len(gnomes)):

        regIndex = gnomes.index(sortedGnomes[i])

        if len(gnomes) > 3:
            if abs(regIndex - i) > 1:
                kingPos = gnomes.index(sortedGnomes[i]) + 1
                break
            elif regIndex != i:
                if regIndex != 0 and (regIndex + 1 < len(gnomes)):
                    if (gnomes[regIndex] > gnomes[regIndex + 1] and gnomes[regIndex] > gnomes[regIndex + 1]
                        ) or (
                            gnomes[regIndex] < gnomes[regIndex + 1] and gnomes[regIndex] < gnomes[regIndex - 1]):
                        kingPos = gnomes.index(sortedGnomes[i]) + 1
                elif regIndex == 0:
                    if gnomes[regIndex] > gnomes[regIndex + 1]:
                        kingPos = gnomes.index(sortedGnomes[i]) + 1
                elif regIndex + 1 > len(gnomes):
                    if gnomes[regIndex] < gnomes[regIndex - 1]:
                        kingPos = gnomes.index(sortedGnomes[i]) + 1
        else:
            kingPos = 1

    print(kingPos)

    test_cases -= 1