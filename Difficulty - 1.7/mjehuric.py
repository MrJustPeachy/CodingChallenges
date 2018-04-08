data = [int(n) for n in input().strip().split()]


def sort(data):

    for i in range(len(data)):
        if i != len(data) - 1:
            if data[i] > data[i + 1]:
                holder = data[i]
                data[i] = data[i + 1]
                data[i + 1] = holder
                for num in data:
                    print('%d ' % num, end='')
                print()

while data != [1, 2, 3, 4, 5]:
    sort(data)