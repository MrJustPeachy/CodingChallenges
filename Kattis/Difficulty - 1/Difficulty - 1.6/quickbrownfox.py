test_cases = int(input().strip())

while test_cases > 0:

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    string = input().strip().lower()

    missingChars = ''

    for letter in alphabet:
        if not string.__contains__(letter):
            missingChars += letter

    if len(missingChars) == 0:
        print('pangram')
    else:
        print('missing %s' % missingChars)

    test_cases -= 1