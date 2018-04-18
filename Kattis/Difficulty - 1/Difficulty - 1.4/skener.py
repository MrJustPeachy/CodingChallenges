params = [int(n) for n in input().strip().split()]

rows = params[0]
columns = params[1]
newRows = params[2]
newColumns = params[3]

message = []

while rows > 0:

    message.append(input().strip())

    rows -= 1

if newColumns > 1:
    for i in range(len(message)):
        newLine = ''

        for char in message[i]:
            newLine += char * newColumns

        message[i] = newLine

if newRows > 1:
    for i in range(len(message)):
        for j in range(1, newRows + 1):
            print(message[i])
else:
    for i in range(len(message)):
        print(message[i])