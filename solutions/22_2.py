import math


def diffs(nums):
    l = len(nums)
    if l < 5:
        return None

    a = nums[l-4] - nums[l-5]
    b = nums[l-3] - nums[l-4]
    c = nums[l-2] - nums[l-3]
    d = nums[l-1] - nums[l-2]

    return f"{a},{b},{c},{d}"


def increment(num):
    num ^= (num * 64)
    num %= 16777216
    num ^= math.floor(num / 32)
    num %= 16777216
    num ^= (num * 2048)
    num %= 16777216

    return num


def tens(num):
    num_str = str(num)
    return int(num_str[len(num_str)-1])


def sim(num, keys):
    secret_nums = [num]
    bananas = [tens(num)]
    seen = set()
    for _ in range(2000):
        new_secret_num = increment(secret_nums[len(secret_nums)-1])
        new_banana = tens(new_secret_num)
        secret_nums.append(new_secret_num)
        bananas.append(new_banana)
        key = diffs(bananas)
        if key != None and key not in seen:
            if key in keys:
                keys[key] += new_banana
            else:
                keys[key] = new_banana
            seen.add(key)


raw_lines = []
with open('./inputs/22.txt') as file:
    raw_lines = file.readlines()

initial = []
for raw_line in raw_lines:
    initial.append(int(raw_line.strip()))

keys = {}
for num in initial:
    sim(num, keys)


max = -1
for key in keys:
    if keys[key] > max:
        max = keys[key]

print(max)
