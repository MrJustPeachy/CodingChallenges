import sys
import operator

variableDict = {}

for line in sys.stdin:

    if line.strip() == '0':
        break

    lineInput = line.strip().split()

    variables = []
    nums = []

    if '=' in lineInput:
        variableDict[lineInput[0]] = int(lineInput[2])
        pass
    else:
        for char in lineInput:
            if char != '+':
                if char.isdigit():
                    nums.append(int(char))
                else:
                    if char in variableDict:
                        nums.append(variableDict[char])
                    else:
                        variables.append(char)

        if sum(nums) > 0:
            print(sum(nums), end='')
        addedString = ''

        for i in range(len(variables)):
            if sum(nums) > 0:
                if i == 0:
                    addedString += ' + ' + variables[i]
                else:
                    addedString += ' + ' + variables[i]
            else:
                if i == 0:
                    addedString += variables[i]
                else:
                    addedString += ' + ' + variables[i]

        print(addedString)
