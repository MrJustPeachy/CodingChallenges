test_cases = int(input().strip())

while test_cases > 0:

    candidates = int(input().strip())

    votesPerCandidate = []

    while candidates > 0:
        votesPerCandidate.append(int(input().strip()))
        candidates -= 1

    maxVoteCount = votesPerCandidate.count(max(votesPerCandidate))
    highestVotes = max(votesPerCandidate)
    highestVotesIndex = votesPerCandidate.index(max(votesPerCandidate)) + 1
    votesPerCandidate.remove(max(votesPerCandidate))
    sumOfOtherVotes = sum(votesPerCandidate)

    if maxVoteCount > 1:
        print('no winner')
    else:
        if highestVotes > sumOfOtherVotes:
            print('majority winner %d' % highestVotesIndex)
        else:
            print('minority winner %d' % highestVotesIndex)

    test_cases -= 1
