from rocket import RocketBoard

board = RocketBoard(4)

board[2] = 30

print(board[2])
print(board[2].get_distance(board[1]))