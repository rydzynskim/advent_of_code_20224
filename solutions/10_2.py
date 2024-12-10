def dfs(row, col, grid):
    height = grid[row][col]
    if height == 9:
        return 1

    rating = 0
    if row - 1 > -1 and height + 1 == grid[row-1][col]:
        rating += dfs(row-1, col, grid)
    if row + 1 < len(grid) and height + 1 == grid[row+1][col]:
        rating += dfs(row+1, col, grid)
    if col - 1 > -1 and height + 1 == grid[row][col-1]:
        rating += dfs(row, col-1, grid)
    if col + 1 < len(grid[0]) and height + 1 == grid[row][col+1]:
        rating += dfs(row, col+1, grid)

    return rating


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
            score += dfs(row, col, grid)

print(score)
