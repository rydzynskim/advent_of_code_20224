def viz(grid, robot):
    reset = "\033[0m"
    magenta = "\033[35m"
    cyan = "\033[36m"
    green = "\033[32m"
    for row in range(len(grid)):
        row_arr = []
        for col in range(len(grid[0])):
            if row == robot[0] and col == robot[1]:
                row_arr.append(f"{green}@{reset}")
            elif grid[row][col] == '#':
                row_arr.append(f"{cyan}#{reset}")
            elif grid[row][col] == '[':
                row_arr.append(f"{magenta}[{reset}")
            elif grid[row][col] == ']':
                row_arr.append(f"{magenta}]{reset}")
            else:
                row_arr.append(".")
        print("".join(row_arr))


def next_pos(row, col, dir):
    if dir == '<':
        return [row, col-1]
    if dir == '^':
        return [row-1, col]
    if dir == '>':
        return [row, col+1]
    if dir == 'v':
        return [row+1, col]
    raise ValueError(f"Invalid dir: {dir}")


def prev_pos(row, col, dir):
    if dir == '<':
        return [row, col+1]
    if dir == '^':
        return [row+1, col]
    if dir == '>':
        return [row, col-1]
    if dir == 'v':
        return [row-1, col]
    raise ValueError(f"Invalid dir: {dir}")


def bfs_box_positions(grid, row, col, dir):
    positions = []
    current = [[row, col]]
    while len(current) > 0:
        next = []
        for c in current:
            n = next_pos(c[0], c[1], dir)
            nv = grid[n[0]][n[1]]
            if nv == '[' or nv == ']':
                next.append(n)
            if dir == '<' or dir == '>':
                continue
            cv = grid[c[0]][c[1]]
            if (cv == ']' or cv == '.') and nv == '[':
                next.append([n[0], n[1]+1])
            if (cv == '[' or cv == '.') and nv == ']':
                next.append([n[0], n[1]-1])
        for n in next:
            positions.append(n)
        current = next
    return positions


def can_move(grid, robot, positions, dir):
    n = next_pos(robot[0], robot[1], dir)
    if grid[n[0]][n[1]] == '#':
        return False
    for pos in positions:
        n = next_pos(pos[0], pos[1], dir)
        if grid[n[0]][n[1]] == '#':
            return False
    return True


def shift(grid, positions, dir):
    pos_str = set()
    for pos in positions:
        pos_str.add(f"{pos[0]},{pos[1]}")

    prev_vals = {}
    cur_vals = {}
    for pos in positions:
        cur_vals[f"{pos[0]},{pos[1]}"] = grid[pos[0]][pos[1]]
        prev = prev_pos(pos[0], pos[1], dir)
        if f"{prev[0]},{prev[1]}" in pos_str:
            prev_vals[f"{pos[0]},{pos[1]}"] = grid[prev[0]][prev[1]]
        else:
            prev_vals[f"{pos[0]},{pos[1]}"] = '.'

    for pos in positions:
        next = next_pos(pos[0], pos[1], dir)
        grid[next[0]][next[1]] = cur_vals[f"{pos[0]},{pos[1]}"]
        grid[pos[0]][pos[1]] = prev_vals[f"{pos[0]},{pos[1]}"]


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
            if square == "#":
                row.append("#")
                row.append("#")
            elif square == ".":
                row.append(".")
                row.append(".")
            elif square == "O":
                row.append("[")
                row.append("]")
            elif square == "@":
                row.append("@")
                row.append(".")
        grid.append(row)

robot = []
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '@':
            grid[row][col] = '.'
            robot = [row, col]


for move in moves:
    positions = bfs_box_positions(grid, robot[0], robot[1], move)
    if can_move(grid, robot, positions, move):
        shift(grid, positions, move)
        robot = next_pos(robot[0], robot[1], move)

total = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '[':
            total += (100 * row + col)
print(total)
