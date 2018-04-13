test_cases = int(input().strip())

while test_cases > 0:

    sequence = [int(n) for n in input().strip().split()]

    numbers = sequence[0]
    sequence.pop(0)

    sortedSequence = sorted(sequence)

    initialDifference = abs(sortedSequence[1] - sortedSequence[0])

    isSequence = True

    for i in range(len(sequence)):
        if i != len(sequence) - 1:
            if abs(sortedSequence[i + 1] - sortedSequence[i]) != initialDifference:
                isSequence = False
                break

    if isSequence and sortedSequence == sequence:
        print('arithmetic')
    elif isSequence and sortedSequence != sequence:
        sortedSequence.reverse()
        if sortedSequence == sequence:
            print('arithmetic')
        else:
            print('permuted arithmetic')
    else:
        print('non-arithmetic')

    test_cases -= 1