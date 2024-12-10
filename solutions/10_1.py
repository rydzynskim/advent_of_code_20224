def dfs(row, col, grid, summits):
    height = grid[row][col]
    if height == 9:
        summits.add(f"{row},{col}")
        return

    if row - 1 > -1 and height + 1 == grid[row-1][col]:
        dfs(row-1, col, grid, summits)
    if row + 1 < len(grid) and height + 1 == grid[row+1][col]:
        dfs(row+1, col, grid, summits)
    if col - 1 > -1 and height + 1 == grid[row][col-1]:
        dfs(row, col-1, grid, summits)
    if col + 1 < len(grid[0]) and height + 1 == grid[row][col+1]:
        dfs(row, col+1, grid, summits)


raw_grid = []
with open('./inputs/10.txt') as file:
    raw_grid = file.readlines()

grid = []
for raw_row in raw_grid:
    row = []
    for point in raw_row.strip():
        row.append(int(point))
    grid.append(row)

score = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == 0:
            summits = set()
            dfs(row, col, grid, summits)
            score += len(summits)

print(score)
