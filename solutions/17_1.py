import math


def combo(op, regs):
    if op >= 0 and op <= 3:
        return op
    elif op == 4:
        return regs['A']
    elif op == 5:
        return regs['B']
    elif op == 6:
        return regs['C']
    else:
        raise ValueError(f"Invalid Combo Operand: {op}")


raw_lines = []
with open('./inputs/17.txt') as file:
    raw_lines = file.readlines()

regs = {}
program = []
saw_blank_line = False
for raw_line in raw_lines:
    stripped = raw_line.strip()
    if len(stripped) == 0:
        saw_blank_line = True
        continue
    if saw_blank_line:
        for inst in stripped.split(': ')[1].split(','):
            program.append(int(inst))
    else:
        split = stripped.split(': ')
        regs[split[0][len(split[0])-1]] = int(split[1])

stdout = []
ip = 0
while ip < len(program):
    inst = program[ip]
    op = None
    if ip+1 < len(program):
        op = program[ip+1]

    if inst == 0:
        regs['A'] = math.floor(regs['A']/2**combo(op, regs))
    elif inst == 1:
        regs['B'] = regs['B'] ^ op
    elif inst == 2:
        regs['B'] = combo(op, regs) % 8
    elif inst == 3:
        if regs['A'] != 0:
            ip = op
            continue
    elif inst == 4:
        regs['B'] = regs['B'] ^ regs['C']
    elif inst == 5:
        stdout.append(f"{combo(op, regs) % 8}")
    elif inst == 6:
        regs['B'] = math.floor(regs['A']/2**combo(op, regs))
    elif inst == 7:
        regs['C'] = math.floor(regs['A']/2**combo(op, regs))
    else:
        raise ValueError(F"Invalid Instruction Code: {inst}")

    ip += 2

print(",".join(stdout))
