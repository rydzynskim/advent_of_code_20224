# returns the distance between 2 points
def dist(p, q):
    return ((p[0]-q[0])**2+(p[1]-q[1])**2)**(1/2)


# given a line and an x value returns the y value
def solve(m, b, x):
    # important to round this to avoid floating point error
    return round((m * x) + b, 6)


# returns the parameters of the line created from the 2 given points
def fit(p, q):
    m = (q[1] - p[1]) / (q[0] - p[0])
    b = p[1] - (m * p[0])
    return [m, b]


def get_locs(points, rows, cols, locs):
    # iterate over all the combinations of antennas
    for i in range(len(points)):
        p = points[i]
        for j in range(i+1, len(points)):
            q = points[j]
            # get the line fitting this pair
            m, b = fit(p, q)
            for x in range(cols):
                y = solve(m, b, x)
                d1 = dist([x, y], p)
                d2 = dist([x, y], q)
                if (y % 1 == 0) and y < rows and y > -1:
                    locs.add(f"{x},{int(y)}")


raw_lines = []
with open('./inputs/8.txt') as file:
    raw_lines = file.readlines()

grid = []
for raw_line in raw_lines:
    stripped = raw_line.strip()
    row = []
    for char in stripped:
        row.append(char)
    grid.append(row)

rows = len(grid)
cols = len(grid[0])
# record the locations of each type of antenna
points = {}
for y in range(rows):
    for x in range(cols):
        if grid[y][x] != ".":
            if grid[y][x] in points:
                points[grid[y][x]].append([x, y])
            else:
                points[grid[y][x]] = [[x, y]]

locs = set()
for key in points:
    # for each type of antenna, get the locations of all the antinodes
    get_locs(points[key], rows, cols, locs)

print(len(locs))
