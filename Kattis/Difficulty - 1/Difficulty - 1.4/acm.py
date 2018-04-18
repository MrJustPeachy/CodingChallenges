import sys

answerDict = {}

solved = 0
totalTime = 0

for line in sys.stdin:

    if line.strip() == '-1':
        break

    data = line.strip().split()

    time = int(data[0])
    problem = data[1]
    status = data[2]

    if status == 'right':
        if problem in answerDict:
            totalTime += answerDict[problem] + time
        else:
            totalTime += time

        solved += 1
    else:
        if problem in answerDict:
            answerDict[problem] += 20
        else:
            answerDict[problem] = 20

print('%d %d' % (solved, totalTime))