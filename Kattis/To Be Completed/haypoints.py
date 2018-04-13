conditions = [int(n) for n in input().strip().split()]
dictionaryLength = conditions[0]
numberOfDescriptions = conditions[1]

hayPointDictionary = {}

while dictionaryLength > 0:
    entry = input().strip().split()
    hayPointDictionary[entry[0]] = 