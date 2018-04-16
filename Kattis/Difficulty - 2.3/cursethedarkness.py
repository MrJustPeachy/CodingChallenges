import math

test_cases = int(input().strip())

while test_cases > 0:

    xBookCoord, yBookCoord = [float(n) for n in input().strip().split()]

    candles = []
    numberOfCandles = int(input().strip())

    while numberOfCandles > 0:

        candles.append([float(n) for n in input().strip().split()])

        numberOfCandles -= 1

    candleClose = False

    for candle in candles:
        distance = math.sqrt(math.pow(candle[0] - xBookCoord, 2) + math.pow(candle[1] - yBookCoord, 2))

        if distance <= 8.0:
            candleClose = True
            break

    if candleClose:
        print('light a candle')
    else:
        print('curse the darkness')

    test_cases -= 1
