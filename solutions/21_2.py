num_pad = {
    "9": [0, 2],
    "8": [0, 1],
    "7": [0, 0],
    "6": [1, 2],
    "5": [1, 1],
    "4": [1, 0],
    "3": [2, 2],
    "2": [2, 1],
    "1": [2, 0],
    "A": [3, 2],
    "0": [3, 1],
    "X": [3, 0],
}
dir_pad = {"A": [0, 2], "^": [0, 1], "X": [0, 0], ">": [1, 2], "v": [1, 1], "<": [1, 0]}


def is_safe(start, path, pad):
    loc = pad[start].copy()
    for move in path:
        if move == "^":
            loc[0] = loc[0] - 1
        elif move == "v":
            loc[0] = loc[0] + 1
        elif move == ">":
            loc[1] = loc[1] + 1
        elif move == "<":
            loc[1] = loc[1] - 1
        if loc[0] == pad["X"][0] and loc[1] == pad["X"][1]:
            return False
    return True


def dict_len(dict):
    total = 0
    for key in dict:
        total += len(key) * dict[key]
    return total


def shortest_path(start, end, pad):
    vert_diff = pad[end][0] - pad[start][0]
    vert_dir = "^" if vert_diff < 0 else "v"
    hor_diff = pad[end][1] - pad[start][1]
    hor_dir = "<" if hor_diff < 0 else ">"
    hor_moves = [hor_dir] * abs(hor_diff) + [vert_dir] * abs(vert_diff)
    vert_moves = [vert_dir] * abs(vert_diff) + [hor_dir] * abs(hor_diff)

    # move horizontal first if we have to move left so we have to
    # move less to generate the following sequence
    if hor_dir == "<":
        if is_safe(start, hor_moves, pad):
            return "".join(hor_moves)
        return "".join(vert_moves)
    if is_safe(start, vert_moves, pad):
        return "".join(vert_moves)
    return "".join(hor_moves)


def get_moves(sequences, pad):
    # notice that a bunch of the sequences are repeating so we can
    # just keep a frequency map instead of iterating over everything
    next = {}
    for sequence in sequences:
        previous = "A"
        freq = sequences[sequence]
        for target in sequence:
            temp = shortest_path(previous, target, pad) + "A"
            if temp in next:
                next[temp] += freq
            else:
                next[temp] = freq
            previous = target
    return next


def solve(sequence):
    p = get_moves({sequence: 1}, num_pad)
    for _ in range(25):
        p = get_moves(p, dir_pad)
    return dict_len(p)


raw_lines = []
with open("./inputs/21.txt") as file:
    raw_lines = file.readlines()

sequences = []
for raw_line in raw_lines:
    sequences.append(raw_line.strip())

complexity = 0
for sequence in sequences:
    complexity += solve(sequence) * int(sequence[:3])

print(complexity)
