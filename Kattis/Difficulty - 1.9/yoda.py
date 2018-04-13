firstNum = input().strip()
secondNum = input().strip()

newFirstNum = ''
newSecondNum = ''

if len(firstNum) > len(secondNum):
    newFirstNum += firstNum[:len(firstNum) - len(secondNum)]
    firstNum = firstNum[len(firstNum) - len(secondNum):]

elif len(secondNum) > len(firstNum):
    newSecondNum += secondNum[:len(secondNum) - len(firstNum)]
    secondNum = secondNum[len(secondNum) - len(firstNum):]

for i in range(len(firstNum)):
    if firstNum[i] == secondNum[i]:
        newFirstNum += firstNum[i]
        newSecondNum += secondNum[i]
    elif firstNum[i] > secondNum[i]:
        newFirstNum += firstNum[i]
    elif secondNum[i] > firstNum[i]:
        newSecondNum += secondNum[i]

if len(newFirstNum) == 0:
    print('YODA')
else:
    if int(newFirstNum) == 0:
        print('0')
    else:
        print(newFirstNum)

if len(newSecondNum) == 0:
    print('YODA')
else:
    if int(newSecondNum) == 0:
        print('0')
    else:
        print(newSecondNum)
