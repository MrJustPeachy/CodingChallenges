import sys

days = 1

customersData = {}

for line in sys.stdin:

    if line.strip() == 'CLOSE':
        customersData = {}

    customer = line.strip().split()

    days += 1
