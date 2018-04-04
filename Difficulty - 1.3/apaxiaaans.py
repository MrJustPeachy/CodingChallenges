import itertools

string = input().strip()

fixed = ''.join(i for i, _ in itertools.groupby(string))

print(fixed)