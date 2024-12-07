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
    for j in range(4, 13):
      if i+j >= len(memory):
        continue

      s = memory[i:i+j]
      if s == "do()":
        valid.append(True)
      elif s == "don't()":
        valid.append(False)
      else:
        digits = check_string(s)
        if digits:
          valid.append(digits)

  return valid

memory = ""
with open('./inputs/3.txt') as file:
  memory = file.read().strip()

total = 0
enabled = True
for elem in parser(memory):
  if type(elem) == bool:
    enabled = elem
  elif enabled:
    total += elem[0] * elem[1]

print(total)