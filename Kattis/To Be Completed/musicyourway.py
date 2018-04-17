import operator

features = input().strip().split()

numberOfInputs = int(input().strip())

songsData = []

while numberOfInputs > 0:

    songsData.append(input().strip().split())

    numberOfInputs -= 1

numberOfSorts = int(input().strip())

sorts = []

while numberOfSorts > 0:

    sorts.append(input().strip())

    numberOfSorts -= 1

for sort in sorts:
    print(' '.join(features))
    sortingIndex = features.index(sort)
    sortedArray = sorted(songsData, key=operator.itemgetter(sortingIndex))
    for data in sortedArray:
        print(' '.join(data))
    print()