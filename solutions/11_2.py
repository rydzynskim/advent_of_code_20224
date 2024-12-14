import math

# Notice that on any iteration, there is a lot of repeating stones.
# If we keep iterate over a frequency map we will perform a lot less
# iterations than if we iterate over everything as is.


def update(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        # convert to int to remove leading zeros
        left = int(stone[:math.floor(len(stone)/2)])
        right = int(stone[math.floor(len(stone)/2):])
        return [str(left), str(right)]
    else:
        return [str(int(stone)*2024)]


stones = {}
with open('./inputs/11.txt') as file:
    temp = file.readlines()[0].strip().split(" ")
    for stone in temp:
        stones[stone] = 1

for _ in range(75):
    next_stones = {}
    for stone in stones:
        freq = stones[stone]
        for key in update(stone):
            if key in next_stones:
                next_stones[key] += freq
            else:
                next_stones[key] = freq
    stones = next_stones

total = 0
for stone in stones:
    total += stones[stone]
print(total)
