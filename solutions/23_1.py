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


raw_lines = []
with open("./inputs/23.txt") as file:
    raw_lines = file.readlines()

connections = {}
for raw_line in raw_lines:
    first, second = raw_line.strip().split("-")
    if first not in connections:
        connections[first] = set([second])
    else:
        connections[first].add(second)
    if second not in connections:
        connections[second] = set([first])
    else:
        connections[second].add(first)


total = 0
seen = set()
for a in connections:
    if a[0] != "t":
        continue
    for b in connections[a]:
        for c in connections[b]:
            if a in connections[c] and f"{a},{b},{c}" not in seen:
                total += 1
                for arr in permute([a, b, c]):
                    seen.add(f"{arr[0]},{arr[1]},{arr[2]}")
print(total)
