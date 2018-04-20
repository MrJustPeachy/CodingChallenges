import sys

filename = 'Prob01.in.txt'

totalMuns = 0.0

for line in open(filename):
    coin, amount = line.strip().split('=')

    amount = int(amount)

    if coin == 'QUARTER':
        totalMuns += 0.25 * amount
    elif coin == 'DIME':
        totalMuns += 0.10 * amount
    elif coin == 'NICKEL':
        totalMuns += 0.05 * amount
    elif coin == 'HALFDOLLAR':
        totalMuns += 0.50 * amount
    elif coin == 'PENNY':
        totalMuns += 0.01 * amount

print('${:.2f}'.format(totalMuns))