def is_safe(report):
  if len(report) < 2:
    return True
  
  decreasing = (report[1]-report[0]) < 0
  for i in range(1, len(report)):
    diff = report[i] - report[i-1]
    if decreasing and (diff < -3 or diff > -1):
      return False
    
    if not decreasing and (diff > 3 or diff < 1):
      return False
    
  return True

raw_lines = []
with open('./inputs/2.txt') as file:
  lines = file.readlines()

reports = []
for line in lines:
  str_report = line.strip().split(" ")
  int_report = []
  for level in str_report:
    int_report.append(int(level))
  reports.append(int_report)

safe = 0
for report in reports:
  if is_safe(report):
    safe += 1

print(safe)
