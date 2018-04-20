# Import file
filename = 'Prob10.in.txt'

for line in open(filename):

    binary = line.strip()
    binary1 = int(binary[:8], 2)
    binary2 = int(binary[8:16], 2)
    binary3 = int(binary[16:24], 2)
    binary4 = int(binary[24:32], 2)

    if 0 <= binary1 <= 127:
        print('%d.%d.%d.%d [CLASS A]' % (binary1, binary2, binary3, binary4))
    elif 128 <= binary1 <= 191:
        print('%d.%d.%d.%d [CLASS B]' % (binary1, binary2, binary3, binary4))
    elif 192 <= binary1 <= 223:
        print('%d.%d.%d.%d [CLASS C]' % (binary1, binary2, binary3, binary4))
    elif 224 <= binary1 <= 239:
        print('%d.%d.%d.%d [CLASS D]' % (binary1, binary2, binary3, binary4))
    elif 240 <= binary1 <= 255:
        print('%d.%d.%d.%d [CLASS E]' % (binary1, binary2, binary3, binary4))
