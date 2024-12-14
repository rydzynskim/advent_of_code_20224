def parse_line(s):
    temp = s.strip().split(':')[1].split(',')
    x = int(temp[0][3:])
    y = int(temp[1][3:])
    return [x, y]


def min_tokens(a, b, target):
    min_cost = 505
    for i in range(101):
        for j in range(101):
            x = a[0] * i + b[0] * j
            y = a[1] * i + b[1] * j
            cost = 3 * i + j
            if x == target[0] and y == target[1] and cost < min_cost:
                min_cost = cost
    return min_cost


raw_lines = []
with open('./inputs/13.txt') as file:
    raw_lines = file.readlines()

games = []
game = []
for raw_line in raw_lines:
    if len(game) == 3:
        games.append(game)
        game = []
        continue

    game.append(parse_line(raw_line))
games.append(game)

total = 0
for game in games:
    cost = min_tokens(game[0], game[1], game[2])
    if cost == 505:
        continue
    total += cost
print(total)
