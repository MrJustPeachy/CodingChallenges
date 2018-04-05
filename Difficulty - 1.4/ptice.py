questions = int(input().strip())

test = input().strip()

Adrian = 'ABC' * 50
Bruno = 'BABC' * 50
Goran = 'CCAABB' * 50

points = [['Adrian', 0], ['Bruno', 0], ['Goran', 0]]

for i in range(0, len(test)):

    if test[i] == Adrian[i]:
        points[0][1] += 1
    if test[i] == Bruno[i]:
        points[1][1] += 1
    if test[i] == Goran[i]:
        points[2][1] += 1

sortedPoints = sorted(points, key=lambda l: l[1], reverse=True)

highScore = sortedPoints[0][1]

print(highScore)

for i in range(len(sortedPoints)):
    if sortedPoints[i][1] == highScore:
        print(sortedPoints[i][0])