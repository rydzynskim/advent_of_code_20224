def possible_pattern(pattern, towels):
    if len(pattern) == 0:
        return True

    for i in range(len(pattern)):
        if pattern[:i+1] in towels and possible_pattern(pattern[i+1:], towels):
            return True

    return False


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
for pattern in patterns:
    if possible_pattern(pattern, towels):
        total += 1

print(total)
