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
print(f'Ranking of the rockets depending of speed: \n {board.get_ranking()}')
print(f'Distance between rockets {distance1} and {distance2} is {board[distance1-1].get_distance(board[distance2-1])}')

score = 0

if board[maxDistance1-1].get_distance(board[maxDistance2-1]) == board.get_max_distance:
    print(f'Congratulation, distance between rockets {maxDistance1} and {maxDistance2} are the bigest')
    score += 1
else:
    print(f'Unfortunately rockets {maxDistance1} and {maxDistance2} are not farthest from each other')


if board[minDistance1-1].get_distance(board[minDistance2-1]) == board.get_min_distance:
    print(f'Congratulation, distance between rockets {minDistance1} and {minDistance2} are least')
    score += 1
else:
    print(f'Unfortunately rockets {minDistance1} and {minDistance2} are not closest from each other')   


statusF = 0
for i in range(len(board.get_fastest_rockets())):
    if board.get_fastest_rockets()[i] == FastestRocket:
        statusF += 1
if statusF > 0:
    print(f'Congratulation, rocket {FastestRocket} is the fastest')
    score += 1
else:
    print(f'Unfortunately rocket {FastestRocket} is not the fastest')


statusS = 0
for i in range(len(board.get_slowest_rockets())):
    if board.get_slowest_rockets()[i] == SlowestRocket:
        statusS += 1
if statusS > 0:
    print(f'Congratulation, rocket {SlowestRocket} is the slowest')
    score += 1
else:
    print(f'Unfortunately rocket {SlowestRocket} is not the slowest')


if score > 0:
    print(f'You win and score {score}!')
else:
    print('You lose :(')

print(board.get_distance_ranking())