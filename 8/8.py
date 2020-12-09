import time

class Inst:
    def __init__(self, inst, val):
        self.inst = inst
        self.val = val
        self.visited = False
        self.times_visited = 0

def parse_input(input_lines):
    instructions = []
    for line in input_lines:
        inst = line.split(' ')[0]
        val = line.split(' ')[1]
        instructions.append(Inst(inst, val))
    return instructions

def run1(instructions):
    flag = True
    idx = 0
    acc = 0
    while flag == True:
        i = instructions[idx].inst
        v = int(instructions[idx].val)
        #print(i,v)
        if instructions[idx].visited == True:
            break
        if i == 'nop':
            instructions[idx].visited = True
            instructions[idx].times_visited += 1
            idx += 1
        elif i == 'acc':
            instructions[idx].visited = True
            instructions[idx].times_visited += 1
            acc += v
            idx += 1
        elif i == 'jmp':
            instructions[idx].visited = True
            instructions[idx].times_visited += 1
            idx += v
    return acc

def run2(instructions):
    flag = True
    idx = 0
    acc = 0
    while flag == True:
        if idx == len(instructions):
            return acc
        if instructions[idx].visited == True:
            return None
        i = instructions[idx].inst
        v = int(instructions[idx].val)
        if i == 'nop':
            instructions[idx].visited = True
            instructions[idx].times_visited += 1
            idx += 1
        elif i == 'acc':
            instructions[idx].visited = True
            instructions[idx].times_visited += 1
            acc += v
            idx += 1
        elif i == 'jmp':
            instructions[idx].visited = True
            instructions[idx].times_visited += 1
            idx += v

with open('./8/8.txt','r') as f:
    input_lines = [line.strip() for line in f]
    instructions = parse_input(input_lines)
    # Part 1
    print('Part 1:')
    print(run1(instructions))
    # Part 2 
    print('Part 2:')
    for i in range(len(input_lines)):
        tmp = input_lines[:]
        if tmp[i].startswith('jmp'):
            tmp[i] = tmp[i].replace('jmp','nop')
        elif tmp[i].startswith('nop'):
            tmp[i] = tmp[i].replace('nop','jmp')
        instructions = parse_input(tmp)
        out = run2(instructions)
        if out:
            print(out)

    