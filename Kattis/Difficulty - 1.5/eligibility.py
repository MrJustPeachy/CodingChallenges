test_cases = int(input().strip())

while test_cases > 0:

    data = [n for n in input().strip().split()]

    name = data[0]
    beganCollege = data[1]
    dateOfBirth = data[2]
    courses = int(data[3])

    if int(beganCollege[:4]) >= 2010:
        print('%s eligible' % name)
    elif int(dateOfBirth[:4]) >= 1991:
        print('%s eligible' % name)
    elif courses < 41:
        print('%s coach petitions' % name)
    else:
        print('%s ineligible' % name)

    test_cases -= 1