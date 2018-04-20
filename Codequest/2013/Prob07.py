# Import file
filename = 'Prob07.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        name, stats = file.readline().strip().split(':')
        statsList = [stat for stat in stats.split(',')]

        singles = 0
        doubles = 0
        triples = 0
        homeRuns = 0
        totalAtBats = 0

        for stat in statsList:
            if stat == 'K':
                totalAtBats += 1
            elif stat == '1B':
                singles += 1
                totalAtBats += 1
            elif stat == '2B':
                doubles += 1
                totalAtBats += 1
            elif stat == '3B':
                triples += 1
                totalAtBats += 1
            elif stat == 'HR':
                homeRuns += 1
                totalAtBats += 1

        if totalAtBats == 0:
            print('%s=0.00' % name)
        else:
            SLG = round(((singles + (2 * doubles) + (3 * triples) + (4 * homeRuns)) / totalAtBats), 3)
            print('{:s}={:.3f}'.format(name, SLG))

        test_cases -= 1