test_input = int(input().strip())

predictedSeconds = 0
actualSeconds = 0

while test_input > 0:

    data = [int(n) for n in input().strip().split()]

    predictedSeconds += (data[0] * 60)
    actualSeconds += data[1]

    test_input -= 1

average = actualSeconds / predictedSeconds

if average > 1:
    print('{:.7f}'.format(actualSeconds / predictedSeconds))
else:
    print('measurement error')