def move(grid, row, col, last_row, last_col):
    if grid[row+1][col] == '.' and (row+1 != last_row or col != last_col):
        return row+1, col
    if grid[row-1][col] == '.' and (row-1 != last_row or col != last_col):
        return row-1, col
    if grid[row][col+1] == '.' and (row != last_row or col+1 != last_col):
        return row, col+1
    if grid[row][col-1] == '.' and (row != last_row or col-1 != last_col):
        return row, col-1
    raise ValueError(f"No available moves at ({row},{col})")


def is_valid(grid, row, col):
    return row > -1 and row < len(grid) and col > -1 and col < len(grid[0])


def s(row, col):
    return f"{row},{col}"


def bfs_cheats(grid, row, col, cheats):
    seen_walls = set()
    cheats[s(row, col)] = 0
    current = [[row, col]]
    steps = 1
    while steps <= 20:
        next = []
        for point in current:
            r = point[0]
            c = point[1]
            if is_valid(grid, r+1, c) and s(r+1, c) not in seen_walls and s(r+1, c) not in cheats:
                if grid[r+1][c] == '.':
                    cheats[s(r+1, c)] = steps
                else:
                    seen_walls.add(s(r+1, c))
                next.append([r+1, c])
            if is_valid(grid, r-1, c) and s(r-1, c) not in seen_walls and s(r-1, c) not in cheats:
                if grid[r-1][c] == '.':
                    cheats[s(r-1, c)] = steps
                else:
                    seen_walls.add(s(r-1, c))
                next.append([r-1, c])
            if is_valid(grid, r, c+1) and s(r, c+1) not in seen_walls and s(r, c+1) not in cheats:
                if grid[r][c+1] == '.':
                    cheats[s(r, c+1)] = steps
                else:
                    seen_walls.add(s(r, c+1))
                next.append([r, c+1])
            if is_valid(grid, r, c-1) and s(r, c-1) not in seen_walls and s(r, c-1) not in cheats:
                if grid[r][c-1] == '.':
                    cheats[s(r, c-1)] = steps
                else:
                    seen_walls.add(s(r, c-1))
                next.append([r, c-1])
        current = next
        steps += 1


raw_lines = []
with open('./inputs/20.txt') as file:
    raw_lines = file.readlines()

grid = []
start_row = None
start_col = None
end_row = None
end_col = None
for row in range(len(raw_lines)):
    new_row = []
    for col in range(len(raw_lines[0].strip())):
        if raw_lines[row][col] == 'E':
            end_row = row
            end_col = col
            new_row.append('.')
        elif raw_lines[row][col] == 'S':
            start_row = row
            start_col = col
            new_row.append('.')
        else:
            new_row.append(raw_lines[row][col])
    grid.append(new_row)


dist = {}
move_counter = 0
prev_row = -1
prev_col = -1
cur_row = end_row
cur_col = end_col
while cur_row != start_row or cur_col != start_col:
    dist[s(cur_row, cur_col)] = move_counter
    new_row, new_col = move(grid, cur_row, cur_col, prev_row, prev_col)
    prev_row = cur_row
    prev_col = cur_col
    cur_row = new_row
    cur_col = new_col
    move_counter += 1
dist[s(cur_row, cur_col)] = move_counter

total = 0
for pos_str in dist:
    row_str, col_str = pos_str.split(',')
    row = int(row_str)
    col = int(col_str)
    cheats = {}
    bfs_cheats(grid, row, col, cheats)
    for cheat in cheats:
        if dist[pos_str] - dist[cheat] - cheats[cheat] >= 100:
            total += 1

print(total)
