# Import file
filename = 'Prob02.in.txt'

for line in open(filename):

    print(line[::-1].strip())
