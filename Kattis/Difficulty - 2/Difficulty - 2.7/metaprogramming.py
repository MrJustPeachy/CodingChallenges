import operator
import sys

variableDict = {}

for line in sys.stdin:

    if line == '\n':
        break

    instruction = line.strip().split()

    if instruction[0] == 'define':
        variableDict[instruction[2]] = int(instruction[1])
    else:
        operation = instruction[2]

        if instruction[1] not in variableDict or instruction[3] not in variableDict:
            print('undefined')
        else:
            vars = [variableDict[instruction[1]], variableDict[instruction[3]]]

            if operation == '<':
                result = str(operator.lt(vars[0], vars[1])).lower()
                print(result)
            elif operation == '>':
                result = str(operator.gt(vars[0], vars[1])).lower()
                print(result)
            else:
                result = str(operator.eq(vars[0], vars[1])).lower()
                print(result)
