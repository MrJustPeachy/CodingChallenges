number = input().strip()

numberList = sorted(number)

sameDigits = -1

if number == '999999':
    sameDigits = 0

for i in range(int(number) + 1, 1000000):
    stringNum = sorted(str(i))

    if len(str(i)) > len(number):
        sameDigits = 0
        break
    else:
        if stringNum == numberList:
            sameDigits = i
            break

if sameDigits == -1:
    print('0')
else:
    print(sameDigits)