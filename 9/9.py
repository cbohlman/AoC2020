import math

def sum_table(input_list):
    hash = set()
    for i in range(len(input_list)):
        for k in range(len(input_list)):
            if i != k:
                hash.add(input_list[i] + input_list[k])
    return hash

with open('./9/9.txt','r') as f:
    tgt = 0
    input_lines = [int(line.strip()) for line in f]
    for i in range(25, len(input_lines)):
        start = i - 25
        end = i
        hash = sum_table(input_lines[start:end])
        if input_lines[i] not in hash:
            tgt = input_lines[i]
            break
    print('Part 1:')
    print(tgt)
    # Part 2
    print('Part 2:')
    for i in range(len(input_lines)):
        s = input_lines[i]
        for j in range(i, len(input_lines)):
            if i != j or i < j:
                s += input_lines[j]
                # print(sum)
                if s == tgt:
                    print(max(input_lines[i:j]) + min(input_lines[i:j]))
                elif s > tgt:
                    break

