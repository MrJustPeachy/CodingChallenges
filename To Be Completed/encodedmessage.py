import math

test_cases = int(input().strip())

while test_cases > 0:

    message = input().strip()

    rowsAndColumns = int(math.sqrt(len(message)))

    messageList = [message[i: i + rowsAndColumns] for i in range(0, len(message), rowsAndColumns)]

    messageListCopy = messageList

    for i in range(len(messageList)):
        for j in range(len(messageList[i])):
            print('I: %d, J: %d' % (i, j))

    test_cases -= 1