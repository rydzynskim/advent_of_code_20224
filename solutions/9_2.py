line = ""
with open('./inputs/9.txt') as file:
    line = file.readlines()[0].strip()


disk = []
file_id = 0
file = True
for char in line:
    for i in range(int(char)):
        if file:
            disk.append(file_id)
        else:
            disk.append('.')
    if file:
        file_id += 1
    file = not file

file_id -= 1
while file_id > -1:
    block_start = None
    block_size = None
    for i in range(len(disk)-1, -1, -1):
        if disk[i] == file_id:
            size = 1
            while disk[i-size] == disk[i]:
                size += 1
            block_start = i - size + 1
            block_size = size
            break

    empty_size = 0
    for i in range(block_start):
        if disk[i] == '.':
            empty_size += 1
        else:
            empty_size = 0

        # we found an empty block that can fit the block we're moving
        if empty_size == block_size:
            for j in range(block_size):
                disk[i-j] = file_id
                disk[block_start+j] = '.'
            break

    file_id -= 1

checksum = 0
for i in range(len(disk)):
    if disk[i] == '.':
        continue
    checksum += (i * disk[i])

print(checksum)
