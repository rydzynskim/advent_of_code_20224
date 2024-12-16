def viz(grid):
    reset = "\033[0m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    green = "\033[32m"
    for row in range(len(grid)):
        row_arr = []
        for col in range(len(grid[0])):
            if grid[row][col] == '@':
                row_arr.append(f"{green}@{reset}")
            elif grid[row][col] == '#':
                row_arr.append(f"{cyan}#{reset}")
            elif grid[row][col] == 'O':
                row_arr.append(f"{magenta}O{reset}")
            else:
                row_arr.append(".")
        print("".join(row_arr))


def next(row, col, dir):
    if dir == '<':
        return [row, col-1]
    if dir == '^':
        return [row-1, col]
    if dir == '>':
        return [row, col+1]
    if dir == 'v':
        return [row+1, col]
    raise ValueError(f"Invalid dir: {dir}")


def shift(grid, robot, dir):
    c = robot
    pv = '.'
    while grid[c[0]][c[1]] != '.':
        temp = grid[c[0]][c[1]]
        grid[c[0]][c[1]] = pv
        pv = temp
        c = next(c[0], c[1], dir)
    grid[c[0]][c[1]] = pv


raw_lines = []
with open('./inputs/15.txt') as file:
    raw_lines = file.readlines()

grid = []
moves = []
parse_moves = False
for raw_line in raw_lines:
    stripped = raw_line.strip()
    if stripped == "":
        parse_moves = True
        continue
    if parse_moves:
        for move in stripped:
            moves.append(move)
    else:
        row = []
        for square in stripped:
            row.append(square)
        grid.append(row)

robot = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '@':
            robot = [row, col]

for move in moves:
    c = [robot[0], robot[1]]
    while True:
        n = next(c[0], c[1], move)
        v = grid[n[0]][n[1]]
        # if the first thing we see is a wall do nothing
        if v == '#':
            break
        # if we see an empty space, shift everything between
        # the robot and that empty space by 1
        if v == '.':
            shift(grid, robot, move)
            robot = next(robot[0], robot[1], move)
            break
        c = n

total = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 'O':
            total += (100 * row + col)
print(total)
