test_cases = int(input().strip())

caseNumber = 1

while test_cases > 0:

    ropeSegments = int(input().strip())

    segments = ([n for n in input().strip().split()])

    if ropeSegments == 1:
        print('Case #%d: 0' % caseNumber)
        caseNumber += 1
        test_cases -= 1

        break



    print(segments)

    test_cases -= 1
