data = [int(n) for n in input().strip().split()]

people = data[0]
chicken = data[1]

if people < chicken:
    if abs(people - chicken) == 1:
        print('Dr. Chaz will have %d piece of chicken left over!' % abs(people - chicken))
    else:
        print('Dr. Chaz will have %d pieces of chicken left over!' % abs(people - chicken))
else:
    if abs(people - chicken) == 1:
        print('Dr. Chaz needs %d more piece of chicken!' % abs(people - chicken))
    else:
        print('Dr. Chaz needs %d more pieces of chicken!' % abs(people - chicken))