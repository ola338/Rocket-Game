from rocket import RocketBoard

amountOfRockets = int(input("Enter the number of rocket: "))
altitude = int(input("Enter the initial altitude: "))
position = int(input("Enter the initial position: "))
distance1 = int(input("Enter the number of rockets to get distance between them: "))
distance2 = int(input())
maxDistance1 = int(input("Guess which rockets are farthest from each other: "))
maxDistance2 = int(input())
minDistance1 = int(input("Guess which rockets are closest to each other: "))
minDistance2 = int(input())
FastestRocket = int(input("Guess which rocket is the fastest: "))
SlowestRocket = int(input("Guess which rocket is the slowest: "))

board = RocketBoard(altitude, position, amountOfRockets)
print(f'Ranking of the rockets: \n {board.get_ranking()}')
print(f'Distance between rockets {distance1} and {distance2} is {board[distance1-1].get_distance(board[distance2-1])}')

if board[maxDistance1-1].get_distance(board[maxDistance2-1]) == board.get_max_distance:
    print(f'Congratulation, distance between rockets {maxDistance1} and {maxDistance2} are the bigest')
else:
    print(f'Unfortunately rockets {maxDistance1} and {maxDistance2} are not farthest from each other')

if board[minDistance1-1].get_distance(board[minDistance2-1]) == board.get_min_distance:
    print(f'Congratulation, distance between rockets {minDistance1} and {minDistance2} are least')
else:
    print(f'Unfortunately rockets {minDistance1} and {minDistance2} are not closest from each other')   

if board.get_fastest_rocket() == FastestRocket:
    print(f'Congratulation, rocket {FastestRocket} is the fastest')
else:
    print(f'Unfortunately rocket {FastestRocket} is not the fastest')

if board.get_slowest_rocket() == SlowestRocket:
    print(f'Congratulation, rocket {SlowestRocket} is the slowest')
else:
    print(f'Unfortunately rocket {SlowestRocket} is not the slowest')


