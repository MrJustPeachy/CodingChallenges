names = input().strip().split('-')

result = ''

for n in names:
    result += n[:1]

print(result)