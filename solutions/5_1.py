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

  if is_safe:
    middle_index = math.floor(len(raw_updates[i])/2)
    total += int(raw_updates[i][middle_index])

print(total)
