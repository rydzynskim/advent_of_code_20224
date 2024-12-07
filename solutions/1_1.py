raw_lines = []
with open('./inputs/1.txt') as file:
  lines = file.readlines()

first = []
second = []
for line in lines:
  nums = line.strip().split("   ")
  first.append(int(nums[0]))
  second.append(int(nums[1]))
first.sort()
second.sort()

distance = 0
for i in range(len(first)):
  distance += abs(first[i]-second[i])

print(distance)
