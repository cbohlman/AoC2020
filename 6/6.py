import re

# with open('6.txt', 'r') as f:
#     input_lines = f.read()
#     input_lines = re.split('\n\n',input_lines)
#     input_lines = [line.replace('\n','') for line in input_lines]
#     count = 0
#     for line in input_lines:
#         count += len(set(line))

# print(count)

with open('6.txt', 'r') as f:
    input_lines = f.read()
    input_lines = re.split('\n\n',input_lines)
    input_lines = [line.split('\n') for line in input_lines]
    count = 0
    for line in input_lines:
        sets = []
        for val in line:
            sets.append(set(val))
        print(sets)
        count += len(set.intersection(*sets))

print(count)