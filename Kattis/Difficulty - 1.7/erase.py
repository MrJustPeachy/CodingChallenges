N = int(input().strip())

originalMessage = input().strip()
deletedMessage = input().strip()

deletionStatus = 'Deletion succeeded'

for i in range(len(originalMessage)):
    if N % 2 == 0:  # Expect the bits to stay the same
        if originalMessage[i] != deletedMessage[i]:
            deletionStatus = 'Deletion failed'
            break
    else: # Bits should be different
        if originalMessage[i] == deletedMessage[i]:
            deletionStatus = 'Deletion failed'
            break

print(deletionStatus)