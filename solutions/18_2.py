SIZE = 70


def has_target(points, target):
    for point in points:
        if point[0] == target[0] and point[1] == target[1]:
            return True
    return False


def add_next(grid, seen, next, row, col):
    if row < 0 or row > SIZE:
        return
    if col < 0 or col > SIZE:
        return
    if grid[row][col] != '.':
        return
    if f"{row},{col}" in seen:
        return

    next.append([row, col])
    seen.add(f"{row},{col}")


raw_lines = []
with open('./inputs/18.txt') as file:
    raw_lines = file.readlines()

bytes = []
for raw_line in raw_lines:
    split = raw_line.strip().split(',')
    bytes.append([int(split[0]), int(split[1])])

grid = []
for i in range(SIZE+1):
    row = []
    for j in range(SIZE+1):
        row.append('.')
    grid.append(row)

for fallen_byte in bytes:
    byte_col, byte_row = fallen_byte
    grid[byte_row][byte_col] = '#'

    seen = set(["0,0"])
    current = [[0, 0]]
    saw_target = False
    while len(current) > 0:
        next = []
        for point in current:
            row = point[0]
            col = point[1]
            add_next(grid, seen, next, row-1, col)
            add_next(grid, seen, next, row+1, col)
            add_next(grid, seen, next, row, col-1)
            add_next(grid, seen, next, row, col+1)
        if has_target(current, [SIZE, SIZE]):
            saw_target = True
            break
        current = next

    if not saw_target:
        print(f"{byte_col},{byte_row}")
        break
