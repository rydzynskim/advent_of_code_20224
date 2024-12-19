def num_ways(pattern, towels, cache):
    if len(pattern) == 0:
        return 1
    if pattern in cache:
        return cache[pattern]

    total = 0
    for i in range(len(pattern)):
        if pattern[:i+1] in towels:
            total += num_ways(pattern[i+1:], towels, cache)

    cache[pattern] = total

    return total


raw_lines = []
with open('./inputs/19.txt') as file:
    raw_lines = file.readlines()

towels = set()
patterns = []
saw_blank_line = False
for raw_line in raw_lines:
    stripped = raw_line.strip()
    if stripped == "":
        saw_blank_line = True
        continue

    if saw_blank_line:
        patterns.append(stripped)
    else:
        for towel in stripped.split(', '):
            towels.add(towel)

total = 0
for i in range(len(patterns)):
    total += num_ways(patterns[i], towels, {})

print(total)
