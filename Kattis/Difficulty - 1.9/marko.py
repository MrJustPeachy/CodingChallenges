words = int(input().strip())

wordList = []

keysDict = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

while words > 0:

    wordList.append(input().strip())

    words -= 1

keys = input().strip()

possibleWords = 0

for word in wordList:
    charInKeys = ''
    if len(keys) == len(word):
        for i in range(len(keys)):
            keyList = keysDict[keys[i]]
            char = word[i]
            if char in keyList:
                charInKeys += char

    if charInKeys == word and len(charInKeys) > 0:
        possibleWords += 1

print(possibleWords)