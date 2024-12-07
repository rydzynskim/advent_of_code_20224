import math

lines = []
with open('./inputs/5.txt') as file:
  lines = file.readlines()

seen_blank = False
rules = {}
updates = []
raw_updates = []
for line in lines:
  stripped = line.strip()
  if len(stripped) == 0:
    seen_blank = True
    continue

  if seen_blank:
    update_freqs = {}
    split_update = stripped.split(",")
    raw_updates.append(split_update)
    for i in range(len(split_update)):
      num = split_update[i]
      update_freqs[num] = i
    updates.append(update_freqs)
  else:
    [a, b] = stripped.split("|")
    if a in rules:
      rules[a].append(b)
    else:
      rules[a] = [b]

total = 0
# iterate over all the updates
for i in range(len(raw_updates)):
  is_safe = True
  # for each number in this specific update
  for num in raw_updates[i]:
    if num not in rules:
      continue
    # verify each rule for this specific number in the update
    for rule in rules[num]:
        if rule in updates[i]:
          if updates[i][rule] < updates[i][num]:
            is_safe = False

    # the numbers that have more rules associated them will
    # be earlier in the reordered list, the below code essentially
    # sorts the nums in update by how many rules they have that
    # pertain to this specific update
  if not is_safe:
    # get the number of pertenant rules for each number
    counts = []
    for num in updates[i]:
      if num not in rules:
        counts.append([num, 0])
        continue
      num_count = 0
      for rule in rules[num]:
        if rule in updates[i]:
          num_count += 1
      counts.append([num, num_count])

    # sort the counts
    counts.sort(key=lambda x: x[1], reverse=True)
    middle_index = math.floor(len(counts)/2)
    total += int(counts[middle_index][0])

print(total)

    
