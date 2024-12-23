def serialize(arr):
    arr.sort()
    return ",".join(arr)


def listify(comp, comp_set):
    return [comp] + list(comp_set)


def combinations(arr, index, result):
    if index == len(arr):
        if len(result) > 0:
            return [result]
        else:
            return []
    w = combinations(arr, index + 1, result + [arr[index]])
    wo = combinations(arr, index + 1, result)
    res = w + wo
    res.sort(key=lambda x: len(x))
    return res


def check(connections, arr):
    for i in arr:
        for j in arr:
            if i != j and j not in connections[i]:
                return False
    return True


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


party = []
for key in connections:
    possible = combinations(listify(key, connections[key]), 0, [])
    for i in range(len(possible) - 1, 0, -1):
        if check(connections, possible[i]) and len(possible[i]) > len(party):
            party = possible[i]
            break

print(serialize(party))
