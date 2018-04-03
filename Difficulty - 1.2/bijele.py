data = input().strip().split()

result = ''

king = 1
queen = 1
rooks = 2
bishops = 2
knights = 2
pawns = 8

king_diff = king - int(data[0])
result += str(king_diff) + " "

queen_diff = queen - int(data[1])
result += str(queen_diff) + " "

rooks_diff = rooks - int(data[2])
result += str(rooks_diff) + " "

bishops_diff = bishops - int(data[3])
result += str(bishops_diff) + " "

knights_diff = knights - int(data[4])
result += str(knights_diff) + " "

pawns_diff = pawns - int(data[5])
result += str(pawns_diff)

print(result)