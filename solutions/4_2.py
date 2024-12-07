def find_cross(words, row, col):
  ne = words[row+2][col]+words[row+1][col+1]+words[row][col+2] == "MAS"
  sw = words[row][col+2]+words[row+1][col+1]+words[row+2][col] == "MAS"
  se = words[row][col]+words[row+1][col+1]+words[row+2][col+2] == "MAS"
  nw = words[row+2][col+2]+words[row+1][col+1]+words[row][col] == "MAS"
  return (ne or sw) and (se or nw)


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
for row in range(len(words)-2):
  for col in range(len(words[0])-2):
    if find_cross(words, row, col):
      seen += 1

print(seen)
