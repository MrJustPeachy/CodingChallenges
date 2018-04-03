text = input().strip().lower().split()

index = []

message = 'yes'

for t in text:
    indices = [i for i, x in enumerate(text) if x == t]
    index.append(indices)

for i in index:
    if len(i) > 1:
        message = 'no'

print(message)