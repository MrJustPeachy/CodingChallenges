from collections import Counter

# Import file
filename = 'Prob12.in.txt'


def f7(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


elements = []

for line in open(filename):

    element = line.strip().split('>')[0]

    if element[:2] != '</' and element not in elements:
        elements.append(element[1:])

mostCommon = Counter(elements).most_common()

for element in f7(elements):
    elementPos = mostCommon.index((element, elements.count(element)))
    print('%s %d' % (element, mostCommon[elementPos][1]))
