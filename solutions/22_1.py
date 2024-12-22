import math


def sim(num):
    for _ in range(2000):
        num ^= (num * 64)
        num %= 16777216
        num ^= math.floor(num / 32)
        num %= 16777216
        num ^= (num * 2048)
        num %= 16777216

    return num


raw_lines = []
with open('./inputs/22.txt') as file:
    raw_lines = file.readlines()

initial = []
for raw_line in raw_lines:
    initial.append(int(raw_line.strip()))

total = 0
for num in initial:
    total += sim(num)

print(total)
