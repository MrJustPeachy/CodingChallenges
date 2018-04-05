words = [word for word in input().strip().split()]

for i in range(len(words)):
    if words[i].__contains__('apa'):
        words[i] = words[i].replace('apa', 'a')
    if words[i].__contains__('epe'):
        words[i] = words[i].replace('epe', 'e')
    if words[i].__contains__('ipi'):
        words[i] = words[i].replace('ipi', 'i')
    if words[i].__contains__('opo'):
        words[i] = words[i].replace('opo', 'o')
    if words[i].__contains__('upu'):
        words[i] = words[i].replace('upu', 'u')

for word in words:
    print(word + ' ', end='')