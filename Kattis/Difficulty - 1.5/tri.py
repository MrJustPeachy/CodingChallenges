data = [int(n) for n in input().strip().split()]

firstNum = data[0]
secondNum = data[1]
thirdNum = data[2]

if firstNum + secondNum == thirdNum:
    print('%d+%d=%d' % (firstNum, secondNum, thirdNum))

elif firstNum - secondNum == thirdNum:
    print('%d-%d=%d' % (firstNum, secondNum, thirdNum))

elif firstNum * secondNum == thirdNum:
    print('%d*%d=%d' % (firstNum, secondNum, thirdNum))

elif firstNum / secondNum == thirdNum:
    print('%d/%d=%d' % (firstNum, secondNum, thirdNum))

elif firstNum == secondNum + thirdNum:
    print('%d=%d+%d' % (firstNum, secondNum, thirdNum))

elif firstNum == secondNum - thirdNum:
    print('%d=%d-%d' % (firstNum, secondNum, thirdNum))

elif firstNum == secondNum / thirdNum:
    print('%d=%d/%d' % (firstNum, secondNum, thirdNum))

elif firstNum == secondNum * thirdNum:
    print('%d=%d*%d' % (firstNum, secondNum, thirdNum))