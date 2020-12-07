import re
import sys

def find_bags(colors, input_lines, alls):
    new_colors = set()
    if len(colors) == 0:
        return
    else:
        for color in colors:
            for line in input_lines:
                s = line.split('bags contain')
                if color in s[1]:
                    alls.add(s[0])
                    new_colors.add(s[0])
        return find_bags(new_colors, input_lines, alls)

def count_bags(num, color, input_lines):
    for line in input_lines:
        s = line.split('bags contain ')
        if color in s[0]:
            if 'no other bags' in line.split('contain')[1]:
                return 1
            else:
                right = s[1].split(', ')
                for rule in right:
                    print(rule)
                    new_num = int(rule[0])
                    # print(new_num)
                    new_color = rule[2:].split('bag')[0]
                    # print(new_color)
                    # new_color = new_color + 'bags'
                    # print(num, color)
                    return 1 + new_num * count_bags(new_num, new_color, input_lines)

if (sys.argv[1] == 'test'):
    file_name = './7/7t.txt'
else:
    file_name = './7/7.txt'
with open(file_name,'r') as f:
    input_lines = [line.strip() for line in f]
    # direct = set()
    # indirect = set()
    # alls = set()
    # for line in input_lines:
    #     s = line.split('bags contain')
    #     if 'shiny gold' in s[1]:
    #         alls.add(s[0])
    #         direct.add(s[0])
    # flag = True
    # find_bags(direct, input_lines, alls)
    # print(len(alls))
    
    # Part 2
    colors = set()
    for line in input_lines:
        s = line.split('bags contain ')
        if 'shiny gold' in s[0]:
            right = s[1].split(', ')
            for rule in right:
                print(rule)
                num = rule[0]
                color = rule[2:].split('bag')[0]
                bag = (num, color)
                colors.add(bag)
    count = 1
    for bag in colors:
        count += int(bag[0]) * count_bags(bag[0], bag[1], input_lines)
    # print(count_bags(1, 'shiny gold', input_lines) - 1)
    print(colors)
    print(count - 1)
