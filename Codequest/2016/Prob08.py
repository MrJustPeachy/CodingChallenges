import operator

# Import file
filename = 'Prob08.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        songsNum = int(file.readline().strip())

        songs = []

        while songsNum > 0:

            song = file.readline().strip().split(' - ')

            if song[1].startswith('The '):
                songs.append([song[1][4:].lower(), song[0], song[1]])
            else:
                songs.append([song[1].lower(), song[0], song[1]])

            songsNum -= 1

        sortedList = sorted(songs, key=operator.itemgetter(0, 1))

        for i in range(len(sortedList)):
            print('%s - %s' % (sortedList[i][1], sortedList[i][2]))

        test_cases -= 1