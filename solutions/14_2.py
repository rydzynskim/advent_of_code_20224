
import matplotlib.pyplot as plt


def sim(p, v, t, w, h):
    x = (p[0] + v[0] * t) % w
    y = (p[1] + v[1] * t) % h
    return [x, y]


def parse_line(s):
    temp = s.strip().split(' ')
    p_str = temp[0][2:].split(',')
    v_str = temp[1][2:].split(',')

    return [[int(p_str[0]), int(p_str[1])], [int(v_str[0]), int(v_str[1])]]


def viz(positions, t):
    x = []
    y = []
    for position in positions:
        x.append(position[0])
        y.append(position[1])

    plt.scatter(x, y)
    plt.title(f"t = {t}")
    plt.show()


def density(positions):
    m = set()
    for position in positions:
        m.add(f"{position[0]},{position[1]}")

    touching = 0
    for position in positions:
        x = position[0]
        y = position[1]
        if f"{x+1},{y}" in m:
            touching += 1
        elif f"{x-1},{y}" in m:
            touching += 1
        elif f"{x},{y+1}" in m:
            touching += 1
        elif f"{x},{y-1}" in m:
            touching += 1

    return touching


w = 101
h = 103
raw_lines = []
with open('./inputs/14.txt') as file:
    raw_lines = file.readlines()

starting = []
for raw_line in raw_lines:
    starting.append(parse_line(raw_line))


t = 0
while True:
    positions = []
    for position in starting:
        positions.append(sim(position[0], position[1], t, w, h))
    # assume when more than half the points are in contact the christmas tree is showing
    if density(positions) > 250:
        break
    t += 1

# visualize to double check
ending = []
for position in starting:
    ending.append(sim(position[0], position[1], t, w, h))

viz(ending, t)
