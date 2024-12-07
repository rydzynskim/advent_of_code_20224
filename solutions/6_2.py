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


def is_valid(row, col, grid):
    return col > -1 and col < len(grid[0]) and row > -1 and row < len(grid)


raw_lines = []
with open('./inputs/6.txt') as file:
    raw_lines = file.readlines()

grid = []
for raw_line in raw_lines:
    line = []
    for char in raw_line.strip():
        line.append(char)
    grid.append(line)

starting_row = 0
starting_col = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == "^":
            starting_row = row
            starting_col = col

# try placing an obstacle at every location and see if it leads to a cycle
obstacles = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        print(f"Progress: {
              round((row*len(grid[0])+col)/(len(grid)*len(grid[0])), 3)}")
        if grid[row][col] != "#" and (col != starting_col or row != starting_row):
            grid[row][col] = "#"
            has_cycle = False
            current_row = starting_row
            current_col = starting_col
            direction = "N"
            positions = set()
            while True:
                next_row, next_col = next_pos(
                    current_row, current_col, direction)
                # move outside of the grid -> we're done
                if not is_valid(next_row, next_col, grid):
                    break

                # obstacle -> turn right
                if grid[next_row][next_col] == "#":
                    direction = next_dir(direction)
                # no obstacle -> move forward
                else:
                    current_row = next_row
                    current_col = next_col

                if f"{current_row},{current_col},{direction}" in positions:
                    has_cycle = True
                    break
                else:
                    positions.add(f"{current_row},{current_col},{direction}")

            if has_cycle:
                obstacles += 1
            grid[row][col] = "."

print(obstacles)
