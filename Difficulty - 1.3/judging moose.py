data = input().strip().split()

left = int(data[0])
right = int(data[1])

if left > 0 or right > 0:
    if left == right:
        print("Even " + str(left * 2))
    elif left > right:
        print("Odd " + str(left * 2))
    elif right > left:
        print("Odd " + str(right * 2))
else:
    print("Not a moose")