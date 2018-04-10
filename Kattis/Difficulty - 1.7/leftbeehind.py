import sys

for line in sys.stdin:

    if line.strip() == '0 0':
        break

    data = [int(n) for n in line.strip().split()]

    sweetJars = data[0]
    sourJars = data[1]

    if sweetJars + sourJars == 13:
        print('Never speak again.')
    elif sweetJars == sourJars:
        print('Undecided.')
    elif sweetJars > sourJars:
        print('To the convention.')
    else:
        print('Left beehind.')
