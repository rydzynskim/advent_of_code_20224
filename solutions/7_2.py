def is_possible(answer, nums, total):
    if len(nums) == 0:
        return answer == total

    concat = is_possible(answer, nums[1:], int(str(total)+str(nums[0])))
    add = is_possible(answer, nums[1:], total+nums[0])
    mul = is_possible(answer, nums[1:], total*nums[0])

    return concat or add or mul


raw_lines = []
with open('./inputs/7.txt') as file:
    raw_lines = file.readlines()

equations = []
for raw_line in raw_lines:
    eq = []
    eq_split = raw_line.strip().split(" ")
    eq.append(int(eq_split[0][:-1]))
    nums = []
    for num in eq_split[1:]:
        nums.append(int(num))
    eq.append(nums)
    equations.append(eq)

total = 0
for equation in equations:
    if is_possible(equation[0], equation[1][1:], equation[1][0]):
        total += equation[0]

print(total)
