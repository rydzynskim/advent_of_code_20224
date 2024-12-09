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

left = 0
right = len(disk) - 1
while True:
    while left < len(disk) and disk[left] != '.':
        left += 1

    while right > -1 and disk[right] == '.':
        right -= 1

    if left >= right:
        break
    disk[left] = disk[right]
    disk[right] = '.'

checksum = 0
for i in range(len(disk)):
    if disk[i] == '.':
        break
    checksum += (i * disk[i])

print(checksum)
