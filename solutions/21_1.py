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


def permute(arr):
    if len(arr) == 0:
        return [[]]
    result = []
    for i in range(len(arr)):
        element = arr[i]
        rest = arr[:i] + arr[i + 1 :]
        for p in permute(rest):
            result.append([element] + p)
    return result


def shortest_paths(start, end, pad):
    vert_diff = pad[end][0] - pad[start][0]
    vert_dir = "^" if vert_diff < 0 else "v"
    hor_diff = pad[end][1] - pad[start][1]
    hor_dir = "<" if hor_diff < 0 else ">"
    moves = [vert_dir] * abs(vert_diff) + [hor_dir] * abs(hor_diff)
    seen = set()
    for path in permute(moves):
        if is_safe(start, path, pad):
            seen.add("".join(path))
    return seen


def get_moves(sequence, pad):
    previous = "A"
    possible_paths = []
    for target in sequence:
        possible_paths.append(shortest_paths(previous, target, pad))
        previous = target
    possibilities = [""]
    for path_set in possible_paths:
        next = []
        for path in path_set:
            for possible in possibilities:
                next.append(possible + path + "A")
        possibilities = next
    return possibilities


def solve(sequence):
    min = float("inf")
    for a in get_moves(sequence, num_pad):
        for b in get_moves(a, dir_pad):
            for c in get_moves(b, dir_pad):
                if len(c) < min:
                    min = len(c)
    return min


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
