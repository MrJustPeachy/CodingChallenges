# Import file
filename = 'Prob04.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        words = file.readline().strip().split('|')
        word1 = words[0]
        word2 = words[1]

        anagram = True

        for letter in word1:
            if letter not in word2:
                anagram = False

        if anagram and word1 != word2:
            print('%s|%s = ANAGRAM' % (word1, word2))
        else:
            print('%s|%s = NOT AN ANAGRAM' % (word1, word2))

        test_cases -= 1