import math


stones = []
with open('./inputs/11.txt') as file:
    stones = file.readlines()[0].strip().split(" ")


for _ in range(25):
    next = []
    for stone in stones:
        if stone == '0':
            next.append('1')
        elif len(stone) % 2 == 0:
            # convert to int to remove leading zeros
            left = int(stone[:math.floor(len(stone)/2)])
            right = int(stone[math.floor(len(stone)/2):])
            next.append(str(left))
            next.append(str(right))
        else:
            next.append(str(int(stone)*2024))
    stones = next

print(len(stones))
