import sys

numbers = []

for line in sys.stdin:

    if line == '\n':
        break

    numbers.append(int(line.strip()))

modulos = []

for n in numbers:
    try:
        index = modulos.index(n % 42)
    except ValueError:
        modulos.append(n % 42)

print(len(modulos))