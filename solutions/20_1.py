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


def possible_cheats(grid, row, col):
    possible = []
    if grid[row+1][col] == '#' and is_valid(grid, row+2, col) and grid[row+2][col] == '.':
        possible.append([row+2, col])
    if grid[row-1][col] == '#' and is_valid(grid, row-2, col) and grid[row-2][col] == '.':
        possible.append([row-2, col])
    if grid[row][col+1] == '#' and is_valid(grid, row, col+2) and grid[row][col+2] == '.':
        possible.append([row, col+2])
    if grid[row][col-1] == '#' and is_valid(grid, row, col-2) and grid[row][col-2] == '.':
        possible.append([row, col-2])
    return possible


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
    dist[f"{cur_row},{cur_col}"] = move_counter
    new_row, new_col = move(grid, cur_row, cur_col, prev_row, prev_col)
    prev_row = cur_row
    prev_col = cur_col
    cur_row = new_row
    cur_col = new_col
    move_counter += 1
dist[f"{cur_row},{cur_col}"] = move_counter

total = 0
for pos_str in dist:
    row_str, col_str = pos_str.split(',')
    row = int(row_str)
    col = int(col_str)
    for cheat in possible_cheats(grid, row, col):
        if dist[pos_str] - dist[f"{cheat[0]},{cheat[1]}"] - 2 >= 100:
            total += 1

print(total)
