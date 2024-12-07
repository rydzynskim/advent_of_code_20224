def check_string(s: str):
  if not s.startswith("mul"):
    return None
  s = s[3:]
  if len(s) < 1:
    return None
  if s[0] != "(" or s[len(s)-1] != ")":
    return None
  nums = s[1:len(s)-1].split(",")
  if len(nums) != 2:
    return None
  if not nums[0].isdigit() or not nums[1].isdigit():
    return None
  
  return [int(nums[0]), int(nums[1])]

def parser(memory):
  valid = []
  for i in range(len(memory)):
    for j in range(8, 13):
      if i+j >= len(memory):
        continue
      digits = check_string(memory[i:i+j])
      if digits:
        valid.append(digits)

  return valid

memory = ""
with open('./inputs/3.txt') as file:
  memory = file.read().strip()

total = 0
for pair in parser(memory):
  total += pair[0] * pair[1]

print(total)