import re
import sys


if (sys.argv[1] == 'test'):
    file_name = './7/7t.txt'
else:
    file_name = './7/7.txt'
with open(file_name,'r') as f:
    g = dict()
    input_lines = [line.strip() for line in f]
    for line in input_lines:
        s = line.split('bags contain ')
        parent = s[0]
        print(parent)
        right = s[1].split(', ')
        colors = []
        for rule in right:
                num = int(rule[0])
                color = rule[2:].split('bag ')[0]
                colors.append((num,color)) 