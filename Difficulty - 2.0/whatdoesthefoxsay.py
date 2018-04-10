test_cases = int(input().strip())

while test_cases > 0:

    originalRecording = input().strip().split()

    animalSounds = []

    whileBreaker = 1

    while whileBreaker > 0:

        animalSound = input().strip().split()[-1]

        if animalSound != 'say?':
            animalSounds.append(animalSound)
        else:
            break

    foxSounds = [sound for sound in originalRecording if sound not in animalSounds]

    for sound in foxSounds:
        print('%s ' % sound, end='')

    print()

    test_cases -= 1