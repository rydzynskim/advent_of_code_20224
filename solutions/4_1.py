def find_word(words, direction, row, col):
  r = len(words)
  c = len(words[0])
  if direction == 'N' and row-3>-1:
    word = words[row][col]+words[row-1][col]+words[row-2][col]+words[row-3][col]
    return word == "XMAS"
  elif direction == 'S' and row+3<r:
    word = words[row][col]+words[row+1][col]+words[row+2][col]+words[row+3][col]
    return word == "XMAS"
  elif direction == 'E' and col+3<c:
    word = words[row][col]+words[row][col+1]+words[row][col+2]+words[row][col+3]
    return word == "XMAS"
  elif direction == 'W' and col-3>-1:
    word = words[row][col]+words[row][col-1]+words[row][col-2]+words[row][col-3]
    return word == "XMAS"
  elif direction == 'NE' and row-3>-1 and col+3<c:
    word = words[row][col]+words[row-1][col+1]+words[row-2][col+2]+words[row-3][col+3]
    return word == "XMAS"
  elif direction == 'NW' and row-3>-1 and col-3>-1:
    word = words[row][col]+words[row-1][col-1]+words[row-2][col-2]+words[row-3][col-3]
    return word == "XMAS"
  elif direction == 'SE' and row+3<r and col+3<c:
    word = words[row][col]+words[row+1][col+1]+words[row+2][col+2]+words[row+3][col+3]
    return word == "XMAS"
  elif direction == 'SW' and row+3<r and col-3>-1:
    word = words[row][col]+words[row+1][col-1]+words[row+2][col-2]+words[row+3][col-3]
    return word == "XMAS"
  else:
    return False

raw_words = []
with open('./inputs/4.txt') as file:
  raw_words = file.readlines()

words = []
for raw_word in raw_words:
  word = []
  for char in raw_word.strip():
    word.append(char)
  words.append(word)

seen = 0
for row in range(len(words)):
  for col in range(len(words[0])):
    if find_word(words, 'N', row, col):
      seen += 1
    if find_word(words, 'S', row, col):
      seen += 1
    if find_word(words, 'E', row, col):
      seen += 1
    if find_word(words, 'W', row, col):
      seen += 1
    if find_word(words, 'NE', row, col):
      seen += 1
    if find_word(words, 'NW', row, col):
      seen += 1
    if find_word(words, 'SE', row, col):
      seen += 1
    if find_word(words, 'SW', row, col):
      seen += 1

print(seen)
