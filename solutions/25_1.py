def parse(lines):
    grid = []
    for line in lines:
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)

    kind = "key" if "".join(grid[0]) == "....." else "lock"
    cols = []
    for col in range(5):
        total = 0
        for row in range(1, 6):
            if grid[row][col] == "#":
                total += 1
        cols.append(str(total))
    return ",".join(cols), kind


def check_fit(key, lock):
    split_key = key.split(",")
    split_lock = lock.split(",")

    for i in range(len(split_key)):
        if int(split_key[i]) + int(split_lock[i]) > 5:
            return False
    return True


raw_lines = []
with open("./inputs/25.txt") as file:
    raw_lines = file.readlines()

keys = set()
locks = set()
counter = 0
while counter < len(raw_lines):
    val, kind = parse(raw_lines[counter : counter + 7])
    if kind == "key":
        keys.add(val)
    else:
        locks.add(val)
    counter += 8

total = 0
for key in keys:
    for lock in locks:
        if check_fit(key, lock):
            total += 1

print(total)
