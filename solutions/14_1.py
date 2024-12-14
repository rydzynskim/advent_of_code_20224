def sim(p, v, t, w, h):
    x = (p[0] + v[0] * t) % w
    y = (p[1] + v[1] * t) % h
    return [x, y]


def parse_line(s):
    temp = s.strip().split(' ')
    p_str = temp[0][2:].split(',')
    v_str = temp[1][2:].split(',')

    return [[int(p_str[0]), int(p_str[1])], [int(v_str[0]), int(v_str[1])]]


w = 101
h = 103
t = 100
raw_lines = []
with open('./inputs/14.txt') as file:
    raw_lines = file.readlines()

starting = []
for raw_line in raw_lines:
    starting.append(parse_line(raw_line))

ending = []
for position in starting:
    ending.append(sim(position[0], position[1], t, w, h))

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for position in ending:
    mid_x = (w - 1) / 2
    mid_y = (h - 1) / 2
    x = position[0]
    y = position[1]
    if x < mid_x and y < mid_y:
        q1 += 1
    elif x > mid_x and y < mid_y:
        q2 += 1
    elif x < mid_x and y > mid_y:
        q3 += 1
    elif x > mid_x and y > mid_y:
        q4 += 1

print(q1*q2*q3*q4)
