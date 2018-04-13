import sys
import operator

variables = {}
operatorDict = {'+': operator.add, '-': operator.sub}

for line in sys.stdin:

    if line.strip() == 'clear':
        break

    instruction = line.strip().split()

    if instruction[0] == 'def':
        variables[instruction[1]] = int(instruction[2])
    else:
        vars = []
        operators = []
        for i in instruction:
            if i == '+' or i == '-':
                operators.append(i)
            elif i != '=' and i != 'calc':
                if i in variables:
                    vars.append([i, int(variables[i])])
                else:
                    vars.append([i, 'unknown'])

        if vars[1].count('unknown') > 0:

            stringList = ''

            for i in range(len(operators)):
                stringList += vars[i][0] + ' ' + operators[i] + ' ' + vars[i + 1][0] + ' '

            print(stringList + '= unknown')
        else:
            result = 0

            stringList = ''
            for i in range(len(operators)):
                result += operatorDict[operators[i]](variables[vars[i][0]], variables[vars[i + 1][0]])
                stringList += vars[i][0] + ' ' + operators[i] + ' ' + vars[i + 1][0] + ' '

            if result in variables:
                print(stringList + '= ' + result)
            else:
                print(stringList + '= unknown')
