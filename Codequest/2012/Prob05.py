import math

# Import file
filename = 'Prob05.in.txt'

with open(filename) as file:

    principal, interestRate, totalMonths, monthsPaid = [float(n) for n in file.readline().strip().split()]

    monthlyPayment = principal * ((interestRate / 1200) / (1 - math.pow((1 + (interestRate / 1200)), totalMonths)))

    newPrincipal = principal - (monthlyPayment - (principal - (interestRate / 1200)))

    print(newPrincipal)