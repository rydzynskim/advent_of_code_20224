raw_lines = []
with open("./inputs/24.txt") as file:
    raw_lines = file.readlines()

evaluated = {}
gates = {}
saw_blank = False
for raw_line in raw_lines:
    stripped = raw_line.strip()
    if len(stripped) == 0:
        saw_blank = True
        continue
    if saw_blank:
        l, r = stripped.split(" -> ")
        f, o, s = l.split(" ")
        gates[r] = [f, s, o]
    else:
        wire, val = stripped.split(": ")
        evaluated[wire] = int(val)


# USE THE SNIPPET BELOW TO DETERMINE THE SWAPS ACCORDING TO THE ALGORITHM:
# a = x[i-1] and y[i-1]
# b = x[i] xor y[i]
# c = last_left and last_right
# d = a or c
# z[i] = b xor d
# last_left = b
# last_right = d
########################################################
# def construct_key(char, num):
#     if num < 10:
#         return char + "0" + str(num)
#     return char + str(num)


# def get_out_wire(gates, in_1, in_2, op):
#     for key in gates:
#         f, s, o = gates[key]
#         if o == op and f == in_1 and s == in_2:
#             return key
#         if o == op and f == in_2 and s == in_1:
#             return key
#     return None


# last_left = "qvn"
# last_right = "sgr"
# for i in range(2, 45):
#     # get what the inputs should be and store them in a, b, c, d
#     a = get_out_wire(gates, construct_key("x", i - 1), construct_key("y", i - 1), "AND")
#     b = get_out_wire(gates, construct_key("x", i), construct_key("y", i), "XOR")
#     c = get_out_wire(gates, last_left, last_right, "AND")
#     d = get_out_wire(gates, a, c, "OR")

#     # get what the inputs are and compare to what they should be
#     f, s, o = gates[construct_key("z", i)]
#     if f == b and s == d and o == "XOR":
#         last_left = b
#         last_right = d
#         continue
#     if f == d and s == b and o == "XOR":
#         last_left = b
#         last_right = d
#         continue

#     # if we need to swap log everything to help determine the swap
#     print(i)
#     print(f, o, s)
#     print(b, "XOR", d)
#     print(last_left, last_right, a, b, c, d)
#     break
# print("NO MORE SWAPS REQUIRED")
########################################################


# USE THE SNIPPET BELOW TO VERIFY THE SWAPS ARE CORRECT
########################################################
swaps = {
    "vvr": "z08",
    "z08": "vvr",
    "rnq": "bkr",
    "bkr": "rnq",
    "tfb": "z28",
    "z28": "tfb",
    "mqh": "z39",
    "z39": "mqh",
}


def construct_bits(vals):
    keys = []
    for key in vals:
        keys.append(key)
    keys.sort(reverse=True)
    res = ""
    for key in keys:
        res += str(vals[key])
    return res


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


unevaluated = {}
for key in gates:
    if key in swaps:
        unevaluated[swaps[key]] = gates[key]
    else:
        unevaluated[key] = gates[key]


while len(unevaluated) > 0:
    ready = set()
    for wire in unevaluated:
        if unevaluated[wire][0] in evaluated and unevaluated[wire][1] in evaluated:
            ready.add(wire)

    for wire in ready:
        f, s, o = unevaluated[wire]
        evaluated[wire] = eval(evaluated[f], evaluated[s], o)
        del unevaluated[wire]

x_vals = {}
y_vals = {}
z_vals = {}
for wire in evaluated:
    if wire[0] == "z":
        z_vals[wire] = evaluated[wire]
    if wire[0] == "x":
        x_vals[wire] = evaluated[wire]
    if wire[0] == "y":
        y_vals[wire] = evaluated[wire]

swapped_wires = []
for key in swaps:
    swapped_wires.append(key)
swapped_wires.sort()

correct_answer = bin_to_dec(construct_bits(x_vals)) + bin_to_dec(construct_bits(y_vals))
actual_answer = bin_to_dec(construct_bits(z_vals))
print(",".join(swapped_wires))
print(f"Is the correct answer: {correct_answer == actual_answer}")
########################################################
