test_cases = int(input().strip())

peopleInBuilding = []

while test_cases > 0:

    case = input().strip().split()
    action = case[0]
    name = case[1]

    if name not in peopleInBuilding:
        if action == 'entry':
            peopleInBuilding.append(name)
            print('%s entered' % name)
        else:
            print('%s exited (ANOMALY)' % name)
    else:
        if action == 'exit':
            peopleInBuilding.remove(name)
            print('%s exited' % name)
        else:
            print('%s entered (ANOMALY)' % name)

    test_cases -= 1