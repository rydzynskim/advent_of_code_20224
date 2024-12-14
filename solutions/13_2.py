def parse_line(s):
    temp = s.strip().split(':')[1].split(',')
    x = int(temp[0][3:])
    y = int(temp[1][3:])
    return [x, y]


# treat like a system of linear equations
# a[0]i + b[0]j = t[0]
# a[1]i + b[1]j = t[1]
def cost(a, b, t):
    num = b[1] * t[0] - b[0] * t[1]
    den = b[1] * a[0] - b[0] * a[1]

    i = num / den
    if i % 1 != 0:
        return -1

    j = (t[1] - a[1] * i) / b[1]
    if j % 1 != 0:
        return -1

    return int(3 * i + j)


raw_lines = []
with open('./inputs/13.txt') as file:
    raw_lines = file.readlines()

games = []
game = []
for raw_line in raw_lines:
    if len(game) == 3:
        game[2][0] += 10**13
        game[2][1] += 10**13
        games.append(game)
        game = []
        continue

    game.append(parse_line(raw_line))
game[2][0] += 10**13
game[2][1] += 10**13
games.append(game)


total = 0
for game in games:
    c = cost(game[0], game[1], game[2])
    if c == -1:
        continue
    total += c
print(total)
