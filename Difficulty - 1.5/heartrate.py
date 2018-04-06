test_cases = int(input().strip())

while test_cases > 0:

    data = [float(n) for n in input().strip().split()]

    beats = data[0]
    seconds = data[1]

    bpm = (60) / seconds

    print(bpm)

    test_cases -= 1