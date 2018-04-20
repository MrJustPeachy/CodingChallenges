import collections

# Import file
filename = 'Prob03.in.txt'

extensions = []

for line in open(filename):

    extensions.append(line.strip().split('.')[1])

mostCommon = collections.Counter(extensions).most_common()

for extension in set(extensions):
    extensionPos = mostCommon.index((extension, extensions.count(extension)))
    print('%s %d' % (extension, mostCommon[extensionPos][1]))
