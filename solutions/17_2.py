import math

'''
This solution is not a general solution to the problem, it is specific to
the given program. Namely, the given program has the following properties:
1. There is a single jump at the end of the program to the first instruction
2. There is a single stdout right before the jump
3. Register A is only updated once per iteration
4. There is no dependencies on register B/C between iterations,
   they can be expressed in terms of register A

This gives us the following constraints:
let A = the value in register A at the start of every iteration
let i = the current iteration
let N = the total number of iterations
let out = a list of the program output for each iteration

i < N:
  (1) floor(A/2**3) > 0
  (2) ((((A mod 8) ^ 3) ^ 5) ^ floor(A/2**((A mod 8) ^ 3))) % 8 = out[i]

i = N
  (1) floor(A/2**3) = 0
  (2) ((((A mod 8) ^ 3) ^ 5) ^ floor(A/2**((A mod 8) ^ 3))) % 8 = out[i]

We can use these constraints to work backwards from the last iteration and eventually
get the initial value for A. For example, we know that going into the last iteration, A
must be in the range [1, 7]. This is because the program ends so dividing by 8 and 
flooring must give 0. We can keep iterating like this, searching over the reduced range
of A for the previous iteration until we get the initial value.

(Not coming up with a generalized solution kinda feels like cheating. However,
I believe this is what they wanted given the specific structure of the input.
Determining the general solution to this problem feels like an actually hard
computing problem.)
'''

PROGRAM = [2, 4, 1, 3, 7, 5, 0, 3, 1, 5, 4, 4, 5, 5, 3, 0]


def s(nums, reverse):
    copy = nums.copy()
    if reverse:
        copy.reverse()
    copy_str = []
    for num in copy:
        copy_str.append(str(num))
    return ",".join(copy_str)


def next_range(a):
    return a*8, a*8+7


def out(a):
    return (((a % 8) ^ 6) ^ math.floor(a/2**((a % 8) ^ 3))) % 8


def back_compute(prev_a, ip, output):
    if ip == -1:
        if s(output, True) == s(PROGRAM, False):
            return prev_a
        return math.inf

    a_min, a_max = next_range(prev_a)
    possible = []
    for a in range(a_min, a_max+1):
        if out(a) == PROGRAM[ip]:
            next_output = output.copy()
            next_output.append(out(a))
            possible.append(back_compute(a, ip-1, next_output))

    if len(possible) > 0:
        return min(possible)
    return math.inf


print(back_compute(0, len(PROGRAM)-1, []))
