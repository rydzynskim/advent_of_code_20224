def is_side(ds, row, col, kind):
    if f"{row},{col}" not in ds:
        return False

    if kind == 0:
        return f"{row-1},{col}" not in ds
    elif kind == 1:
        return f"{row+1},{col}" not in ds
    elif kind == 2:
        return f"{row},{col-1}" not in ds
    elif kind == 3:
        return f"{row},{col+1}" not in ds
    else:
        raise ValueError(f"Invalid side {kind}")


def mark_side(ds, row, col, kind):
    if kind == 0 or kind == 1:
        right_counter = 0
        while is_side(ds, row, col+right_counter, kind):
            ds[f"{row},{col+right_counter}"][kind] = True
            right_counter += 1
        left_counter = 0
        while is_side(ds, row, col-left_counter, kind):
            ds[f"{row},{col-left_counter}"][kind] = True
            left_counter += 1
    elif kind == 2 or kind == 3:
        up_counter = 0
        while is_side(ds, row-up_counter, col, kind):
            ds[f"{row-up_counter},{col}"][kind] = True
            up_counter += 1
        down_counter = 0
        while is_side(ds, row+down_counter, col, kind):
            ds[f"{row+down_counter},{col}"][kind] = True
            down_counter += 1
    else:
        raise ValueError(f"Invalid side {kind}")


def sides(region):
    ds = {}
    for square in region:
        ds[square] = [False, False, False, False]  # top, bottom, left, right

    total = 0
    for square in region:
        temp = square.split(",")
        row = int(temp[0])
        col = int(temp[1])
        marked = ds[square]
        if f"{row-1},{col}" not in region and not marked[0]:
            total += 1
            mark_side(ds, row, col, 0)

        if f"{row+1},{col}" not in region and not marked[1]:
            total += 1
            mark_side(ds, row, col, 1)

        if f"{row},{col-1}" not in region and not marked[2]:
            total += 1
            mark_side(ds, row, col, 2)

        if f"{row},{col+1}" not in region and not marked[3]:
            total += 1
            mark_side(ds, row, col, 3)

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
    price += len(region) * sides(region)
print(price)
