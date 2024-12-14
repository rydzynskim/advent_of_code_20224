def perimeter(region):
    total = 0
    for square in region:
        temp = square.split(",")
        row = int(temp[0])
        col = int(temp[1])
        if f"{row-1},{col}" not in region:
            total += 1
        if f"{row+1},{col}" not in region:
            total += 1
        if f"{row},{col-1}" not in region:
            total += 1
        if f"{row},{col+1}" not in region:
            total += 1

    return total


def add_next(seen, plot, crop, row, col, next):
    if row < 0 or row > len(plot) - 1:
        return
    if col < 0 or col > len(plot[0]) - 1:
        return
    if seen[row][col]:
        return
    if plot[row][col] != crop:
        return

    seen[row][col] = True
    next.append([row, col])


raw_plot = []
with open('./inputs/12.txt') as file:
    raw_plot = file.readlines()

plot = []
seen = []
for raw_row in raw_plot:
    row = []
    seen_row = []
    for square in raw_row.strip():
        row.append(square)
        seen_row.append(False)
    plot.append(row)
    seen.append(seen_row)

regions = []
for row in range(len(plot)):
    for col in range(len(plot[0])):
        # if this square is already in a region continue
        if seen[row][col]:
            continue

        # bfs all the squares in this region
        current = [[row, col]]
        crop = plot[row][col]
        new_region = set()
        while len(current) > 0:
            next = []
            for square in current:
                new_region.add(f"{square[0]},{square[1]}")
                add_next(seen, plot, crop, square[0]+1, square[1], next)
                add_next(seen, plot, crop, square[0]-1, square[1], next)
                add_next(seen, plot, crop, square[0], square[1]+1, next)
                add_next(seen, plot, crop, square[0], square[1]-1, next)
            current = next
        regions.append(new_region)

price = 0
for region in regions:
    price += len(region) * perimeter(region)
print(price)
