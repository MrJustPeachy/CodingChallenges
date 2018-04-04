data = input().strip().split()

first_number = int(data[0][::-1])
second_number = int(data[1][::-1])

if first_number > second_number:
    print(first_number)
else:
    print(second_number)
