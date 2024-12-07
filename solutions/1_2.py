raw_lines = []
with open('./inputs/1.txt') as file:
  lines = file.readlines()

first = []
second_freqs = {}
for line in lines:
  nums = line.strip().split("   ")
  first_num = int(nums[0])
  second_num = int(nums[1])

  first.append(first_num)
  if second_num in second_freqs:
    second_freqs[second_num] += 1
  else:
    second_freqs[second_num] = 1

similarity = 0
for num in first:
  freq = 0
  if num in second_freqs:
    similarity += num * second_freqs[num]

print(similarity)
