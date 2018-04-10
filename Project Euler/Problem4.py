'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

palindromes = []

for i in reversed(range(100, 1000)):
    for j in reversed(range(100, 1000)):
        product = i * j
        if str(product) == str(product)[::-1]:
            palindromes.append(product)
            break

print(sorted(palindromes)[-1])