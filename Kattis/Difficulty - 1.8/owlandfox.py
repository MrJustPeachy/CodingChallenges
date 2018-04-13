test_cases = int(input().strip())


def sumNum(num):
    n = 0
    while num:
        n, num = n + num % 10, num // 10
    return n


def findClosestNum(num, sOfNums):
    closestNum = 0

    if sOfNums != 1:
        for i in reversed(range(0, number)):
            sumOfOtherNum = sumNum(i)
            if sumOfNums - 1 == sumOfOtherNum:
                closestNum = i
                return closestNum
    else:
        return closestNum


while test_cases > 0:

    number = int(input().strip())
    sumOfNums = sumNum(number)

    closest = findClosestNum(number, sumOfNums)

    print(closest)

    test_cases -= 1
