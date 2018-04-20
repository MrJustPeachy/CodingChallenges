# Import file
filename = 'Prob06.in.txt'

wordDict = {
    'a': 'Alpha',
    'b': 'Bravo',
    'c': 'Charlie',
    'd': 'Delta',
    'e': 'Echo',
    'f': 'Foxtrot',
    'g': 'Golf',
    'h': 'Hotel',
    'i': 'India',
    'j': 'Juliet',
    'k': 'Kilo',
    'l': 'Lima',
    'm': 'Mike',
    'n': 'November',
    'o': 'Oscar',
    'p': 'Papa',
    'q': 'Quebec',
    'r': 'Romeo',
    's': 'Sierra',
    't': 'Tango',
    'u': 'Uniform',
    'v': 'Victor',
    'w': 'Whiskey',
    'x': 'Xray',
    'y': 'Yankee',
    'z': 'Zulu',
    ' ': ' '
}

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        wordNum = int(file.readline().strip())

        words = []

        while wordNum > 0:

            words.append(file.readline().strip())

            wordNum -= 1

        for word in words:
            phoneticSentence = []
            for char in word.lower():
                phoneticSentence.append(wordDict[char])
            joinedSentence = '-'.join(phoneticSentence)
            joinedSentence = joinedSentence.replace('- -', ' ')
            print(joinedSentence)
        test_cases -= 1