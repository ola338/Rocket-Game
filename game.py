from rocket import RocketBoard

amountOfRockets = int(input("Enter the number of rocket: "))
altitude = int(input("Enter the initial altitude: "))
position = int(input("Enter the initial position: "))

board = RocketBoard(altitude, position, amountOfRockets)

print(board[2].get_distance(board[1]))
print(board.get_max_distance())
print(board.get_min_distance())
print(board.get_ranking())