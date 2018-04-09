message = input().strip().split()

aeWords = 0

for word in message:
    if 'ae' in word:
        aeWords += 1

ratio = aeWords / len(message)

if ratio >= .4:
    print('dae ae ju traeligt va')
else:
    print('haer talar vi rikssvenska')