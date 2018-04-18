from fractions import Fraction

# 5/9(F - 32)

fraction = [int(n) for n in input().strip().split('/')]

celsius = (5/9) * (Fraction(fraction[0] / fraction[1]) - 32)

celsius = Fraction(celsius).limit_denominator()

if str(celsius).count('/') != 1:
    print('%d/1' % celsius)
else:
    print(celsius)
