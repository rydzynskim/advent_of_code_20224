def next_pos(row, col, direction):
    if direction == "N":
        return [row-1, col]
    elif direction == "E":
        return [row, col+1]
    elif direction == "S":
        return [row+1, col]
    elif direction == "W":
        return [row, col-1]
    else:
        raise TypeError(f"Invalid Direction: {direction}")


def next_dir(direction):
    if direction == "N":
        return "E"
    elif direction == "E":
        return "S"
    elif direction == "S":
        return "W"
    elif direction == "W":
        return "N"
    else:
        raise TypeError(f"Invalid Direction: {direction}")


raw_lines = []
with open('./inputs/6.txt') as file:
    raw_lines = file.readlines()

grid = []
for raw_line in raw_lines:
    line = []
    for char in raw_line.strip():
        line.append(char)
    grid.append(line)

current_row = 0
current_col = 0
direction = "N"
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "^":
            current_row = row
            current_col = col
            grid[row][col] = "X"

while True:
    next_row, next_col = next_pos(current_row, current_col, direction)
    # move outside of the grid -> we're done
    if next_col == -1 or next_col == len(grid[0]) or next_row == -1 or next_row == len(grid):
        break

    # obstacle -> turn right
    if grid[next_row][next_col] == "#":
        direction = next_dir(direction)
    # no obstacle -> move forward
    else:
        current_row = next_row
        current_col = next_col
        grid[current_row][current_col] = "X"

spaces = 0
for line in grid:
    for space in line:
        if space == "X":
            spaces += 1

print(spaces)
