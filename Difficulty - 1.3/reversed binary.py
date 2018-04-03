number = input().strip()

binary = bin(int(number))[2:][::-1]

print(int(binary, 2))