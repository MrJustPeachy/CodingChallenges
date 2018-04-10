test_cases = int(input().strip())

while test_cases > 0:

    data = [float(n) for n in input().strip().split()]

    beats = data[0]
    seconds = data[1]

    bpm = (60 * beats) / seconds
    timeBetweenBeats = beats / seconds
    apbm = 60 / seconds

    print('ABPM: {:.4f}, BPM: {:.4f}, ABPM+:{:.4f}'.format(apbm, bpm, timeBetweenBeats))

    test_cases -= 1
