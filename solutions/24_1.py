def eval(f, s, o):
    if o == "XOR":
        return f ^ s
    if o == "AND":
        return f and s
    if o == "OR":
        return f or s
    raise ValueError(f"Unsupported Op: {o}")


def bin_to_dec(bin):
    dec = 0
    for i in range(len(bin)):
        dec += int(bin[len(bin) - 1 - i]) * 2**i
    return dec


raw_lines = []
with open("./inputs/24.txt") as file:
    raw_lines = file.readlines()

evaluated = {}
unevaluated = {}
saw_blank = False
for raw_line in raw_lines:
    stripped = raw_line.strip()
    if len(stripped) == 0:
        saw_blank = True
        continue
    if saw_blank:
        l, r = stripped.split(" -> ")
        f, o, s = l.split(" ")
        unevaluated[r] = [f, s, o]
    else:
        wire, val = stripped.split(": ")
        evaluated[wire] = int(val)

while len(unevaluated) > 0:
    ready = set()
    for wire in unevaluated:
        if unevaluated[wire][0] in evaluated and unevaluated[wire][1] in evaluated:
            ready.add(wire)

    for wire in ready:
        f, s, o = unevaluated[wire]
        evaluated[wire] = eval(evaluated[f], evaluated[s], o)
        del unevaluated[wire]

interesting = []
for wire in evaluated:
    if wire[0] == "z":
        interesting.append(wire)

out = ""
interesting.sort(reverse=True)
for wire in interesting:
    out += str(evaluated[wire])

print(bin_to_dec(out))
